from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database
import database
import time

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

@relation_ctrl.route('/judge', methods=['GET', 'POST'])
def judge():
    username = request.args.get('username')
    if request.method == 'POST':
        context = request.form.get('context')

        message_db = database.get_message_database()
        timm = time.localtime()
        message_db.add_message(username, str(timm.tm_year)+','+str(timm.tm_mon)+','+str(timm.tm_mday),context)
        return redirect(url_for('index_ctrl.index'))

    return render_template('judge.html',username=username)
