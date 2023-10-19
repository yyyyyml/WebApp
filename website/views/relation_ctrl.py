from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database

relation_ctrl = Blueprint('relation_ctrl', __name__)

# 添加新路由
@relation_ctrl.route('/favorites')
def favorites():
    return render_template('favorites.html')

@relation_ctrl.route('/history')
def history():
    # 在这里获取用户的历史记录并渲染history.html模板
    # 示例：user_history = get_user_history(username)
    return render_template('history.html')
