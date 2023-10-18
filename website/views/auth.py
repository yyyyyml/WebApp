from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_db = get_user_database()
        user = user_db.get_user(username)

        if user and user['password'] == password:
            session['user'] = username
            if user['permission'] == 'user':
                return redirect(url_for('home.index'))
            else:
                return redirect(url_for('home.manage'))

        flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_db = get_user_database()
        existing_user = user_db.get_user(username)

        if existing_user:
            flash('Username already exists. Choose a different one.', 'danger')
        else:
            # Hash the password before storing it
            hashed_password = password
            user_db.add_user(username, hashed_password)
            flash('Registration successful!', 'success')
            return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth.route('/profile')
def profile():
    if 'user' in session:
        username = session['user']
        user_db = get_user_database()
        user = user_db.get_user(username)
        return render_template('profile.html', user=user)
    return 'You are not logged in'
