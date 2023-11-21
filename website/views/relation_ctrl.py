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
    webs = web_favorite.get_web_favorite(username)
    web_total = database.get_web_item_database()
    web_all = []
    for web in webs:
        web_title = web_total.get_web_title(web['link'])
        web_res = web | web_title
        web_all.append(web_res)
    
    return render_template('favorites.html',username=username,web_all=web_all,current_page='web')

@relation_ctrl.route('/favorites_lit')
def favorites_lit():
    username = request.args.get('username')
    lit_favorite = database.get_literature_favorite_database()
    lits = lit_favorite.get_literature_favorite(username)
    lit_total = database.get_literature_item_database()
    lit_all = []
    for lit in lits:
        lit_title = lit_total.get_lit_title(lit['link'])
        lit_res = lit | lit_title
        lit_all.append(lit_res)
    
    return render_template('favorites_lit.html',username=username,lit_all=lit_all,current_page='lit')

@relation_ctrl.route('/history')
def history():

    username = request.args.get('username')
    web_history = database.get_web_browse_database()
    webs = web_history.get_web_browse(username)
    web_total = database.get_web_item_database()
    web_all = []
    for web in webs:
        web_title = web_total.get_web_title(web['link'])
        web_res = web | web_title
        web_all.append(web_res)
    
    return render_template('history.html',username=username,web_all=web_all,current_page='web')

@relation_ctrl.route('/history_lit')
def history_lit():

    username = request.args.get('username')
    
    lit_history = database.get_literature_browse_database()
    lits = lit_history.get_literature_browse(username)
    lit_total = database.get_literature_item_database()
    lit_all = []
    for lit in lits:
        lit_title = lit_total.get_lit_title(lit['link'])
        lit_res = lit | lit_title
        lit_all.append(lit_res)
    
    return render_template('history_lit.html',username=username,lit_all=lit_all,current_page='lit')

@relation_ctrl.route('/del_web')
def del_web():
    nid = request.args.get('id')
    username = request.args.get('username')
    web = database.get_web_browse_database()
    web.delete_web_browse(nid)
    web_history = database.get_web_browse_database()
    webs = web_history.get_web_browse(username)
    web_total = database.get_web_item_database()
    web_all = []
    for web in webs:
        web_title = web_total.get_web_title(web['link'])
        web_res = web | web_title
        web_all.append(web_res)
    
    return render_template('history.html',username=username,web_all=web_all,current_page='web')

@relation_ctrl.route('/del_lit')
def del_lit():
    nid = request.args.get('id')
    username = request.args.get('username')
    lit = database.get_literature_browse_database()
    lit.delete_literature_browse(nid)
    
    lit_history = database.get_literature_browse_database()
    lits = lit_history.get_literature_browse(username)
    lit_total = database.get_literature_item_database()
    lit_all = []
    for lit in lits:
        lit_title = lit_total.get_lit_title(lit['link'])
        lit_res = lit | lit_title
        lit_all.append(lit_res)
    
    return render_template('history_lit.html',username=username,lit_all=lit_all,current_page='lit')

@relation_ctrl.route('/del_web_favor')
def del_web_favor():
    nid = request.args.get('id')
    username = request.args.get('username')
    web = database.get_web_favorite_database()
    web.delete_web_favorite(nid)
    web_favorite = database.get_web_favorite_database()
    webs = web_favorite.get_web_favorite(username)
    web_total = database.get_web_item_database()
    web_all = []
    for web in webs:
        web_title = web_total.get_web_title(web['link'])
        web_res = web | web_title
        web_all.append(web_res)
    
    return render_template('favorites.html',username=username,web_all=web_all,current_page='web')

@relation_ctrl.route('/del_lit_favor')
def del_lit_favor():
    nid = request.args.get('id')
    username = request.args.get('username')
    lit = database.get_literature_favorite_database()
    lit.delete_literature_favorite(nid)
    
    lit_favorite = database.get_literature_favorite_database()
    lits = lit_favorite.get_literature_favorite(username)
    lit_total = database.get_literature_item_database()
    lit_all = []
    for lit in lits:
        lit_title = lit_total.get_lit_title(lit['link'])
        lit_res = lit | lit_title
        lit_all.append(lit_res)
    
    return render_template('favorites_lit.html',username=username,lit_all=lit_all,current_page='lit')

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

@relation_ctrl.route('/browse_no_item')
def browse_no_item():
    url = request.args.get('url')
    search_type = request.args.get('search_type')
    username = request.args.get('username')
    title = request.args.get('title')
    # print(username)
    if search_type == 'web':
        web_db = database.get_web_browse_database()
        time = datetime.datetime.now()
        time_now = str(time.year) + '.' + str(time.month) + '.' + str(time.day) + ',' + str(time.hour) + ':' + str(
            time.minute)
        web_db.add_web_browse(username, url, time_now)
        # print('done')
        return redirect(url)
    elif search_type == 'literature':
        lit_db = database.get_literature_browse_database()
        time = datetime.datetime.now()
        time_now = str(time.year) + '.' + str(time.month) + '.' + str(time.day) + ',' + str(time.hour) + ':' + str(
            time.minute)
        lit_db.add_literature_browse(username, url, time_now)
        return redirect(url)
