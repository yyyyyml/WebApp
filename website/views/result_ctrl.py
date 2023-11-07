from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import database
import google1
import baidu1
import json
import datetime
from pprint import pprint

# from google import google_scholar_search

result_ctrl = Blueprint('result_ctrl', __name__)


@result_ctrl.route('/search_results')
def search_results():
    query = request.args.get('q')
    search_type = request.args.get('search_type')
    pn = request.args.get('pn')
    username = request.args.get('username')
    # print(username)
    # print(type(pn))
    pn = int(pn)
    if search_type == 'web':
        result = baidu1.baidu_search(query=query, pn=pn)
        pprint(result)
        if len(result) == 0:
            return render_template('web_error.html')
        else:
            d = dict()
            dr = dict()
            web_db = database.get_web_item_database()
            for i in range(1, len(result)):
                d[i] = result[i]
            for j in range(len(result[0]["results"])):
                dr[j] = result[0]["results"][j]
            for i in range(2,len(result)):
                for j in range(1,len(result)-i):
                    webj = web_db.get_web(result[j]['title'])
                    webj1 = web_db.get_web(result[j+1]['title'])
                    if webj is not None and webj1 is not None and webj['likes']<webj1['likes']:
                        result[j],result[j+1] = result[j+1],result[j]
                    elif webj is None and webj1 is not None:
                        result[j], result[j + 1] = result[j + 1], result[j]
            dlike = dict()
            for i in range(1,4):
                dlike[i] = result[i]


            for i in range(2,len(result)):
                for j in range(1,len(result)-i):
                    webj = web_db.get_web(result[j]['title'])
                    webj1 = web_db.get_web(result[j+1]['title'])
                    if webj is not None and webj1 is not None and webj['favorites']<webj1['favorites']:
                        result[j],result[j+1] = result[j+1],result[j]
                    elif webj is None and webj1 is not None:
                        result[j], result[j + 1] = result[j + 1], result[j]
            dfav = dict()
            for i in range(1,4):
                dfav[i] = result[i]


            for i in range(2,len(result)):
                for j in range(1,len(result)-i):
                    webj = web_db.get_web(result[j]['title'])
                    webj1 = web_db.get_web(result[j+1]['title'])
                    if webj is not None and webj1 is not None and webj['browses']<webj1['browses']:
                        result[j],result[j+1] = result[j+1],result[j]
                    elif webj is None and webj1 is not None:
                        result[j], result[j + 1] = result[j + 1], result[j]
            dbr = dict()
            for i in range(1,4):
                dbr[i] = result[i]

            return render_template('web_search_results.html', dic=d, relate=dr, query=query, search_type=search_type,
                                   dlike=dlike,dbr=dbr,dfav=dfav,
                                   pn=pn, username=username)
    elif search_type == 'literature':
        result = google1.google_scholar_search(query, pn)
        if len(result) == 0:
            return render_template('web_error.html')
        else:
            d = dict()
            dr = dict()
            for i in range(len(result)):
                d[i] = result[i]
            lit_db = database.get_literature_item_database()
            for i in range(1,len(result)):
                for j in range(0,len(result)-i):
                    webj = lit_db.get_lit(result[j]['title'])
                    webj1 = lit_db.get_lit(result[j+1]['title'])
                    if webj is not None and webj1 is not None and webj['likes']<webj1['likes']:
                        result[j],result[j+1] = result[j+1],result[j]
                    elif webj is None and webj1 is not None:
                        result[j], result[j + 1] = result[j + 1], result[j]
            dlike = dict()
            for i in range(0,3):
                dlike[i] = result[i]

            for i in range(1,len(result)):
                for j in range(0,len(result)-i):
                    webj = lit_db.get_lit(result[j]['title'])
                    webj1 = lit_db.get_lit(result[j+1]['title'])
                    if webj is not None and webj1 is not None and webj['favorites']<webj1['favorites']:
                        result[j],result[j+1] = result[j+1],result[j]
                    elif webj is None and webj1 is not None:
                        result[j], result[j + 1] = result[j + 1], result[j]
            dfav = dict()
            for i in range(0,3):
                dfav[i] = result[i]


            for i in range(1,len(result)):
                for j in range(0,len(result)-i):
                    webj = lit_db.get_lit(result[j]['title'])
                    webj1 = lit_db.get_lit(result[j+1]['title'])
                    if webj is not None and webj1 is not None and webj['browses']<webj1['browses']:
                        result[j],result[j+1] = result[j+1],result[j]
                    elif webj is None and webj1 is not None:
                        result[j], result[j + 1] = result[j + 1], result[j]
            dbr = dict()
            for i in range(0,3):
                dbr[i] = result[i]
            return render_template('literature_search_results.html', dic=d, query=query, search_type=search_type,
                                   dlike=dlike,dbr=dbr,dfav=dfav, pn=pn,
                                   username=username)


@result_ctrl.route('/good')
def good():
    url = request.args.get('url')
    title = request.args.get('title')
    query = request.args.get('query')
    search_type = request.args.get('search_type')
    pn = request.args.get('pn')
    username = request.args.get('username')
    if search_type == 'web':
        origin = request.args.get('origin')
        snippet = request.args.get('snippet')
        time_origin = request.args.get('time_origin')
        web_db = database.get_web_item_database()
        web = web_db.get_web(title)
        if web == None:
            web_db.add_web_item(url, title, origin, snippet, time_origin, 1, 0, 0)
        else:
            web_db.update_web_item(web['id'], url, web['title'], web['origin'], web['snippet'], web['time_origin'],
                                   web['likes'] + 1, web['favorites'], web['browses'])
        return redirect(
            '/search_results?q=' + query + '&search_type=' + search_type + '&pn=' + pn + '&username=' + username)
    elif search_type == 'literature':
        snippet = request.args.get('snippet')
        author = request.args.get('author')
        #summary_path = request.args.get('summary_path')
        cites = request.args.get('cites')
        pdf_link = request.args.get('pdf_link')
        # summary_path = request.args.get('summary_path')
        lit_db = database.get_literature_item_database()
        lit = lit_db.get_lit(title)
        if lit == None:
            lit_db.add_literature_item(url, title, pdf_link, snippet,author,None,cites, 1, 0, 0)
        else:
            lit_db.update_literature_item(lit['id'], url, lit['title'], lit['link_pdf'], lit['snippet'], lit['author'],
                                          lit['summary_path'], lit['cites'],
                                          lit['likes'] + 1, lit['favorites'], lit['browses'])
        return redirect(
            '/search_results?q=' + query + '&search_type=' + search_type + '&pn=' + pn + '&username=' + username)


@result_ctrl.route('/bad')
def bad():
    url = request.args.get('url')
    title = request.args.get('title')
    query = request.args.get('query')
    search_type = request.args.get('search_type')
    pn = request.args.get('pn')
    username = request.args.get('username')
    if search_type == 'web':
        origin = request.args.get('origin')
        snippet = request.args.get('snippet')
        time_origin = request.args.get('time_origin')
        web_db = database.get_web_item_database()
        web = web_db.get_web(title)
        if web == None:
            web_db.add_web_item(url, title, origin, snippet, time_origin, -1, 0, 0)
        else:
            web_db.update_web_item(web['id'], url, web['title'], web['origin'], web['snippet'], web['time_origin'],
                                   web['likes'] - 1, web['favorites'], web['browses'])
        return redirect(
            '/search_results?q=' + query + '&search_type=' + search_type + '&pn=' + pn + '&username=' + username)
    elif search_type == 'literature':
        snippet = request.args.get('snippet')
        author = request.args.get('author')
        #summary_path = request.args.get('summary_path')
        cites = request.args.get('cites')
        pdf_link = request.args.get('pdf_link')
        # summary_path = request.args.get('summary_path')
        lit_db = database.get_literature_item_database()
        lit = lit_db.get_lit(title)
        if lit == None:
            lit_db.add_literature_item(url, title, pdf_link, snippet,author,None,cites, -1, 0, 0)
        else:
            lit_db.update_literature_item(lit['id'], url, lit['title'], lit['link_pdf'], lit['snippet'], lit['author'],
                                          lit['summary_path'], lit['cites'],
                                          lit['likes'] - 1, lit['favorites'], lit['browses'])
        return redirect(
            '/search_results?q=' + query + '&search_type=' + search_type + '&pn=' + pn + '&username=' + username)


@result_ctrl.route('/browse')
def browse():
    url = request.args.get('url')
    search_type = request.args.get('search_type')
    username = request.args.get('username')
    title = request.args.get('title')
    # print(username)
    if search_type == 'web':
        origin = request.args.get('origin')
        snippet = request.args.get('snippet')
        time_origin = request.args.get('time_origin')
        web_db = database.get_web_browse_database()
        web_db_item = database.get_web_item_database()
        web = web_db_item.get_web(title)
        if web == None:
            web_db_item.add_web_item(url, title,origin,snippet,time_origin, 0, 0, 1)
        else:
            web_db_item.update_web_item(web['id'], url, web['title'], web['origin'], web['snippet'], web['time_origin'],
                                   web['likes'], web['favorites'], web['browses'] + 1)
        time = datetime.datetime.now()
        time_now = str(time.year) + '.' + str(time.month) + '.' + str(time.day) + ',' + str(time.hour) + ':' + str(
            time.minute)
        web_db.add_web_browse(username, url, time_now)
        # print('done')
        return redirect(url)
    elif search_type == 'literature':
        snippet = request.args.get('snippet')
        author = request.args.get('author')
        #summary_path = request.args.get('summary_path')
        cites = request.args.get('cites')
        pdf_link = request.args.get('pdf_link')
        # summary_path = request.args.get('summary_path')
        lit_db = database.get_literature_browse_database()
        lit_db_item = database.get_literature_item_database()
        lit = lit_db_item.get_lit(title)
        if lit == None:
            lit_db_item.add_literature_item(url, title, pdf_link, snippet,author,None,cites, 0, 0, 1)
        else:
            lit_db_item.update_literature_item(lit['id'], url, lit['title'], lit['link_pdf'], lit['snippet'],
                                               lit['author'],
                                               lit['summary_path'], lit['cites'],
                                               lit['likes'], lit['favorites'], lit['browses'] + 1)
        time = datetime.datetime.now()
        time_now = str(time.year) + '.' + str(time.month) + '.' + str(time.day) + ',' + str(time.hour) + ':' + str(
            time.minute)
        lit_db.add_literature_browse(username, url, time_now)
        return redirect(url)


@result_ctrl.route('/favorite')
def favorite():
    url = request.args.get('url')
    title = request.args.get('title')
    query = request.args.get('query')
    search_type = request.args.get('search_type')
    username = request.args.get('username')
    pn = request.args.get('pn')
    # print(username)
    if search_type == 'web':
        origin = request.args.get('origin')
        snippet = request.args.get('snippet')
        time_origin = request.args.get('time_origin')
        web_db = database.get_web_favorite_database()
        web_db_item = database.get_web_item_database()
        web = web_db_item.get_web(title)
        if web == None:
            web_db_item.add_web_item(url, title, origin,snippet,time_origin, 0, 1, 0)
        else:
            web_db.update_web_item(web['id'], url, web['title'], web['origin'], web['snippet'], web['time_origin'],
                                   web['likes'], web['favorites'] + 1, web['browses'])
        time = datetime.datetime.now()
        time_now = str(time.year) + '.' + str(time.month) + '.' + str(time.day) + ',' + str(time.hour) + ':' + str(
            time.minute)
        web_db.add_web_favorite(username, url, time_now)
        # print('done')
        return redirect(
            '/search_results?q=' + query + '&search_type=' + search_type + '&pn=' + pn + '&username=' + username)
    elif search_type == 'literature':
        snippet = request.args.get('snippet')
        author = request.args.get('author')
        #summary_path = request.args.get('summary_path')
        cites = request.args.get('cites')
        pdf_link = request.args.get('pdf_link')
        # summary_path = request.args.get('summary_path')
        lit_db = database.get_literature_favorite_database()
        lit_db_item = database.get_literature_item_database()
        lit = lit_db_item.get_lit(title)
        if lit == None:
            lit_db_item.add_literature_item(url, title, pdf_link,snippet,author,None,cites, 0, 1, 0)
        else:
            lit_db_item.update_literature_item(lit['id'], url, lit['title'], lit['link_pdf'], lit['snippet'],
                                               lit['author'],
                                               lit['summary_path'], lit['cites'],
                                               lit['likes'], lit['favorites'] + 1, lit['browses'])
        time = datetime.datetime.now()
        time_now = str(time.year) + '.' + str(time.month) + '.' + str(time.day) + ',' + str(time.hour) + ':' + str(
            time.minute)
        lit_db.add_literature_favorite(username, url, time_now)
        return redirect(
            '/search_results?q=' + query + '&search_type=' + search_type + '&pn=' + pn + '&username=' + username)
