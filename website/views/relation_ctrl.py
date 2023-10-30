from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database
import database
import datetime
import time

relation_ctrl = Blueprint('relation_ctrl', __name__)

# 添加新路由
@relation_ctrl.route('/favorites')
def favorites():
    username = request.args.get('username')
    web_favorite = database.get_web_favorite_database()
    web = web_favorite.get_all_favorite()
    lit_favorite = database.get_literature_favorite_database()
    lit = lit_favorite.get_all_favorite()
    
    return render_template('favorites.html',username=username,web=web,lit=lit)

@relation_ctrl.route('/history')
def history():
    # 在这里获取用户的历史记录并渲染history.html模板
    # 示例：user_history = get_user_history(username)
    username = request.args.get('username')
    web_history = database.get_web_browse_database()
    web = web_history.get_all_history()
    lit_history = database.get_literature_browse_database()
    lit = lit_history.get_all_history()
    
    return render_template('history.html',username=username,web=web,lit=lit)

@relation_ctrl.route('/del_web')
def del_web():
    nid = request.args.get('id')
    web = database.get_web_browse_database()
    web.delete_web_browse(nid)

    return redirect("/history")

@relation_ctrl.route('/del_lit')
def del_lit():
    nid = request.args.get('id')
    web = database.get_literature_browse_database()
    web.delete_literature_browse(nid)

    return redirect("/history")

@relation_ctrl.route('/del_web_favor')
def del_web_favor():
    nid = request.args.get('id')
    web = database.get_web_favorite_database()
    web.delete_web_favorite(nid)

    return redirect("/favorites")

@relation_ctrl.route('/del_lit_favor')
def del_lit_favor():
    nid = request.args.get('id')
    web = database.get_literature_favorite_database()
    web.delete_literature_favorite(nid)

    return redirect("/favorites")

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
