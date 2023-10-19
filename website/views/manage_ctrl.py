from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database

manage_ctrl = Blueprint('manage_ctrl', __name__)


@manage_ctrl.route('/manage')
def manage():
    # 在这里获取用户的历史记录并渲染history.html模板
    # 示例：user_history = get_user_history(username)
    return render_template('manage.html')