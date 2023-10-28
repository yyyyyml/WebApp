# manage_ctrl.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database, get_message_database

manage_ctrl = Blueprint('manage_ctrl', __name__)

@manage_ctrl.route('/manage')
def manage():
    return render_template('manage.html')

@manage_ctrl.route('/logout_user', methods=['POST'])
def logout_user():
    if request.method == 'POST':
        username = request.form.get('username')
        # 执行注销用户的操作
        user_db = get_user_database()
        user_db.delete_user(username)
        flash(f'User {username} has been logged out.', 'success')

    return redirect(url_for('manage_ctrl.manage_user'))

@manage_ctrl.route('/update_permission', methods=['POST'])
def update_permission():
    if request.method == 'POST':
        username = request.form.get('username')
        new_permission = request.form.get('new_permission')
        # 执行修改用户权限的操作
        user_db = get_user_database()
        user_db.update_permission(username, new_permission)
        flash(f'Permission for user {username} has been updated.', 'success')

    return redirect(url_for('manage_ctrl.manage_user'))

@manage_ctrl.route('/manage_user')
def manage_user():
    # 获取所有用户信息
    user_db = get_user_database()
    users = user_db.get_all_users()
    return render_template('manage_user.html', users=users)

@manage_ctrl.route('/manage_status')
def manage_status():
   # 获取平台状态信息，这里使用示例数据
    server_runtime = "10 days"
    online_users = 50
    server_load = "80%"
    available_storage = "500 GB"

    return render_template('manage_status.html', server_runtime=server_runtime, online_users=online_users, server_load=server_load, available_storage=available_storage)

@manage_ctrl.route('/manage_feedback')
def manage_feedback():
    # 获取用户反馈信息
    # 在这里获取相应的数据
    message_db = get_message_database()
    messages = message_db.get_all_messages()
    return render_template('manage_feedback.html', messages=messages)
