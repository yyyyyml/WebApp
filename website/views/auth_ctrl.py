from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database

auth_ctrl = Blueprint('auth_ctrl', __name__)

@auth_ctrl.route('/')
def root():
    return redirect(url_for('auth_ctrl.login'))

@auth_ctrl.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_db = get_user_database()
        user = user_db.get_user(username)

        if user and user['password'] == password:
            session['user'] = username
            
            if user['permission'] == 'user':
                session['users'] = session.get('users', [])  # 初始化一个空的用户列表
                session['users'].append(username)  # 将用户添加到列表
                return redirect(url_for('index_ctrl.index'))
            else:
                return redirect(url_for('manage_ctrl.manage_status', username=username, current_page ='manage_status'))

        flash('登录失败！请检查用户名和密码', 'danger')

    return render_template('login.html')

@auth_ctrl.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_db = get_user_database()
        existing_user = user_db.get_user(username)

        if existing_user:
            flash('注册失败，用户名已存在！', 'danger')
        else:
            # Hash the password before storing it
            hashed_password = password
            user_db.add_user(username, hashed_password)
            flash('已成功注册，请登录！', 'success')
            return redirect(url_for('auth_ctrl.login'))

    return render_template('register.html')

@auth_ctrl.route('/profile')
def profile():
    if 'user' in session:
        username = session['user']
        user_db = get_user_database()
        user = user_db.get_user(username)
        return render_template('profile.html', user=user)
    return '您未登录'

# 清除用户登录状态
@auth_ctrl.route('/logout')
def logout():
    username = request.args.get('username')
    
    if 'users' in session:
        if username in session['users']:
            session['users'].remove(username)  # Remove the user from the list in session
            session.modified = True  # Mark session as modified
            print(session['users'])
            
    return redirect(url_for('auth_ctrl.login'))