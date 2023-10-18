from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database

home = Blueprint('home', __name__)

@home.route('/index')
def index():
    if 'user' in session:
        username = session['user']
        user_db = get_user_database()
        user = user_db.get_user(username)
        return render_template('index.html', user=user)
    return redirect(url_for('auth.login'))
    
@home.route('/search_results')
def search_results():
    query = request.args.get('q')
    search_type = request.args.get('search_type')

    if search_type == 'web':
        return render_template('web_search_results.html')
    elif search_type == 'literature':
        return render_template('literature_search_results.html')

# 添加新路由
@home.route('/favorites')
def favorites():
    return render_template('favorites.html')

@home.route('/history')
def history():
    # 在这里获取用户的历史记录并渲染history.html模板
    # 示例：user_history = get_user_history(username)
    return render_template('history.html')

@home.route('/manage')
def manage():
    # 在这里获取用户的历史记录并渲染history.html模板
    # 示例：user_history = get_user_history(username)
    return render_template('manage.html')