from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database

index_ctrl = Blueprint('index_ctrl', __name__)

@index_ctrl.route('/index')
def index():
    if 'user' in session:
        username = session['user']
        user_db = get_user_database()
        user = user_db.get_user(username)
        return render_template('index.html', user=user)
    return redirect(url_for('auth_ctrl.login'))