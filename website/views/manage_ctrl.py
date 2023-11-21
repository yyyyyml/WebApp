# manage_ctrl.py
import os
import platform
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database, get_message_database
import psutil
import subprocess
import datetime



manage_ctrl = Blueprint('manage_ctrl', __name__)

@manage_ctrl.route('/manage')
def manage():
    username = request.args.get('username')
    return render_template('manage.html', username=username)

@manage_ctrl.route('/logout_user', methods=['POST'])
def logout_user():
    if request.method == 'POST':
        username = request.form.get('username')
        rootname = request.args.get('rootname')
        # 执行注销用户的操作
        user_db = get_user_database()
        user_db.delete_user(username)
        # flash(f'用户{username}已被注销', 'success')

    return redirect(url_for('manage_ctrl.manage_user', username=rootname))

@manage_ctrl.route('/update_permission', methods=['POST'])
def update_permission():
    if request.method == 'POST':
        username = request.form.get('username')
        rootname = request.args.get('rootname')
        new_permission = request.form.get('new_permission')
        # 执行修改用户权限的操作
        user_db = get_user_database()
        user_db.update_permission(username, new_permission)
        # flash(f'用户{username}的权限已更新', 'success')

    return redirect(url_for('manage_ctrl.manage_user', username=rootname))

@manage_ctrl.route('/manage_user')
def manage_user():
    # 获取所有用户信息
    username = request.args.get('username')
    current_page = request.args.get('current_page')
    user_db = get_user_database()
    users = user_db.get_all_users()
    return render_template('manage_user.html', users=users, username=username, current_page=current_page)

@manage_ctrl.route('/manage_status')
def manage_status():
    username = request.args.get('username')
    current_page = request.args.get('current_page')
   # 获取平台状态信息，这里使用示例数据
    server_runtime = get_server_runtime()
    online_users = get_online_users()
    system_info = get_system_info()
    cpu_usage = get_total_cpu_usage()
    memory_usage = get_memory_usage()
    available_storage = get_available_storage()

    return render_template('manage_status.html', username=username, current_page=current_page, server_runtime=server_runtime, online_users=online_users, system_info=system_info, cpu_usage=cpu_usage, memory_usage=memory_usage, available_storage=available_storage)

@manage_ctrl.route('/manage_feedback')
def manage_feedback():
    username = request.args.get('username')
    current_page = request.args.get('current_page')
    # 获取用户反馈信息
    message_db = get_message_database()
    messages = message_db.get_all_messages()
    return render_template('manage_feedback.html', username=username, current_page=current_page, messages=messages)

def get_system_info():
    system_info = {
        'OS Version': platform.platform(),
        'Hostname': platform.node()
    }
    return platform.platform()

# 获取可用磁盘存储
def get_available_storage():
    partition = psutil.disk_usage("/")
    return f"{partition.free / (1024**3):.2f} GB"

def get_server_runtime():
    boot_time_timestamp = psutil.boot_time()
    current_time = datetime.datetime.now()
    uptime = current_time - datetime.datetime.fromtimestamp(boot_time_timestamp)
    days, seconds = uptime.days, uptime.seconds
    hours = seconds // 3600
    return f"{days} d  {hours} h"

def get_total_cpu_usage():
    # logical_cores = psutil.cpu_percent(interval=1, percpu=True)
    # return logical_cores
    logical_cores = psutil.cpu_percent(interval=1, percpu=True)
    total_usage = sum(logical_cores) / len(logical_cores)
    return f"{total_usage:.2f}%"

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    total_memory = memory_info.total
    available_memory = memory_info.available
    used_memory = total_memory - available_memory
    memory_percent = (used_memory / total_memory) * 100
    return f"{memory_percent:.2f}%"

def get_online_users():
    if 'users' in session:
        users = session['users']  # 获取用户列表
        print(users)
        return f'{len(users)}'
    else:
        return 0
