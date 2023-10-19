from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database

result_ctrl = Blueprint('result_ctrl', __name__)
    
@result_ctrl.route('/search_results')
def search_results():
    query = request.args.get('q')
    search_type = request.args.get('search_type')

    if search_type == 'web':
        return render_template('web_search_results.html')
    elif search_type == 'literature':
        return render_template('literature_search_results.html')
