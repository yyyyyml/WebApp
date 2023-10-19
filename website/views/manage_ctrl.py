# manage_ctrl.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database

manage_ctrl = Blueprint('manage_ctrl', __name__)

@manage_ctrl.route('/manage')
def manage():
    # 获取所有用户信息
    user_db = get_user_database()
    users = user_db.get_all_users()

    return render_template('manage.html', users=users)

@manage_ctrl.route('/logout_user', methods=['POST'])
def logout_user():
    if request.method == 'POST':
        username = request.form.get('username')
        # 执行注销用户的操作
        user_db = get_user_database()
        user_db.delete_user(username)
        flash(f'User {username} has been logged out.', 'success')

    return redirect(url_for('manage_ctrl.manage'))

@manage_ctrl.route('/update_permission', methods=['POST'])
def update_permission():
    if request.method == 'POST':
        username = request.form.get('username')
        new_permission = request.form.get('new_permission')
        # 执行修改用户权限的操作
        user_db = get_user_database()
        user_db.update_permission(username, new_permission)
        flash(f'Permission for user {username} has been updated.', 'success')

    return redirect(url_for('manage_ctrl.manage'))
