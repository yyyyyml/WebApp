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
        web_search_db = database.get_web_search_database()
        # 检查数据库中是否存在结果
        existing_result = web_search_db.get_web_search_result(query, pn)

        if existing_result:
            # 如果结果已存在，使用已有结果
            result = existing_result['result']
            print("已有的搜索结果")
        else:
            # 如果结果不存在，调用搜索函数
            result = baidu1.baidu_search(query=query, pn=pn)
            pprint(result)
            if len(result) <=1:
                return render_template('web_error.html')
            else:
                # 将新结果存入数据库
                web_search_db.add_web_search_result(query, pn, result)
            
        
        
        web_fav_db = database.get_web_favorite_database()
        
        favlist1 = web_fav_db.get_web_favorite(username)
        web_like_db = database.get_web_like_database()
        likelist1= web_like_db.get_web_like(username)
        likemask=[]
        favmask=[]
        for i in range(1,len(result)):
            flaglike = False
            for j in range(len(likelist1)):
                if result[i]['title']==likelist1[j]['title']:
                    likemask.append(1)
                    flaglike=True
                    break
            if not flaglike:
                likemask.append(0)
        for i in range(1,len(result)):
            flagfav = False
            for j in range(len(favlist1)):
                if result[i]['title']==favlist1[j]['title']:
                    favmask.append(1)
                    flagfav=True
                    break
            if not flagfav:
                favmask.append(0)

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
        likelist = []
        lm = []
        fm = []
        for i in range(1,4):
            dlike[i] = result[i]
            web = web_db.get_web(result[i]['title'])
            if web is not None:
                likelist.append(web['likes'])
            else:
                likelist.append(0)
            flaglike = False
            for j in range(len(likelist1)):
                if result[i]['title'] == likelist1[j]['title']:
                    lm.append(1)
                    flaglike = True
                    break
            if not flaglike:
                lm.append(0)
            flagfav = False
            for j in range(len(favlist1)):
                if result[i]['title'] == favlist1[j]['title']:
                    fm.append(1)
                    flagfav = True
                    break
            if not flagfav:
                fm.append(0)


        for i in range(2,len(result)):
            for j in range(1,len(result)-i):
                webj = web_db.get_web(result[j]['title'])
                webj1 = web_db.get_web(result[j+1]['title'])
                if webj is not None and webj1 is not None and webj['favorites']<webj1['favorites']:
                    result[j],result[j+1] = result[j+1],result[j]
                elif webj is None and webj1 is not None:
                    result[j], result[j + 1] = result[j + 1], result[j]
        dfav = dict()
        favlist = []
        lm1=[]
        fm1=[]
        for i in range(1,4):
            dfav[i] = result[i]
            web = web_db.get_web(result[i]['title'])
            if web is not None:
                favlist.append(web['favorites'])
            else:
                favlist.append(0)
            flaglike = False
            for j in range(len(likelist1)):
                if result[i]['title'] == likelist1[j]['title']:
                    lm1.append(1)
                    flaglike = True
                    break
            if not flaglike:
                lm1.append(0)
            flagfav = False
            for j in range(len(favlist1)):
                if result[i]['title'] == favlist1[j]['title']:
                    fm1.append(1)
                    flagfav = True
                    break
            if not flagfav:
                fm1.append(0)


        for i in range(2,len(result)):
            for j in range(1,len(result)-i):
                webj = web_db.get_web(result[j]['title'])
                webj1 = web_db.get_web(result[j+1]['title'])
                if webj is not None and webj1 is not None and webj['browses']<webj1['browses']:
                    result[j],result[j+1] = result[j+1],result[j]
                elif webj is None and webj1 is not None:
                    result[j], result[j + 1] = result[j + 1], result[j]
        dbr = dict()
        brlist = []
        lm2=[]
        fm2=[]
        for i in range(1,4):
            dbr[i] = result[i]
            web = web_db.get_web(result[i]['title'])
            if web is not None:
                brlist.append(web['browses'])
            else:
                brlist.append(0)
            flaglike = False
            for j in range(len(likelist1)):
                if result[i]['title'] == likelist1[j]['title']:
                    lm2.append(1)
                    flaglike = True
                    break
            if not flaglike:
                lm2.append(0)
            flagfav = False
            for j in range(len(favlist1)):
                if result[i]['title'] == favlist1[j]['title']:
                    fm2.append(1)
                    flagfav = True
                    break
            if not flagfav:
                fm2.append(0)

        return render_template('web_search_results.html', dic=d, relate=dr, query=query, search_type=search_type,
                                dlike=dlike,dbr=dbr,dfav=dfav,likelist=likelist,favlist=favlist,brlist = brlist,
                                likemask=likemask,favmask=favmask,lm=lm,fm=fm,lm1=lm1,fm1=fm1,lm2=lm2,fm2=fm2,
                                pn=pn, username=username)
    elif search_type == 'literature':
        lit_search_db = database.get_literature_search_database()
        # 检查数据库中是否存在结果
        existing_result = lit_search_db.get_literature_search_result(query, pn)

        if existing_result:
            # 如果结果已存在，使用已有结果
            result = existing_result['result']
            print("已有的搜索结果")
        else:
            # 如果结果不存在，调用搜索函数
            result = google1.google_scholar_search(query, pn)
            pprint(result)
            if len(result) == 0:
                return render_template('web_error.html')
            else:
                # 将新结果存入数据库
                lit_search_db.add_literature_search_result(query, pn, result)
        
       
        web_fav_db = database.get_literature_favorite_database()
        favlist1 = web_fav_db.get_literature_favorite(username)
        web_like_db = database.get_literature_like_database()
        likelist1 = web_like_db.get_literature_like(username)
        likemask = []
        favmask = []
        for i in range(0, len(result)):
            flaglike = False
            for j in range(len(likelist1)):
                if result[i]['link'] == likelist1[j]['link']:
                    likemask.append(1)
                    flaglike = True
                    break
            if not flaglike:
                likemask.append(0)
        for i in range(0, len(result)):
            flagfav = False
            for j in range(len(favlist1)):
                if result[i]['link'] == favlist1[j]['link']:
                    favmask.append(1)
                    flagfav = True
                    break
            if not flagfav:
                favmask.append(0)
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
        likelist = []
        lm=[]
        fm=[]
        for i in range(0,3):
            dlike[i] = result[i]
            web = lit_db.get_lit(result[i]['title'])
            if web is not None:
                likelist.append(web['likes'])
            else:
                likelist.append(0)
            flaglike = False
            for j in range(len(likelist1)):
                if result[i]['link'] == likelist1[j]['link']:
                    lm.append(1)
                    flaglike = True
                    break
            if not flaglike:
                lm.append(0)
            flagfav = False
            for j in range(len(favlist1)):
                if result[i]['link'] == favlist1[j]['link']:
                    fm.append(1)
                    flagfav = True
                    break
            if not flagfav:
                fm.append(0)

        for i in range(1,len(result)):
            for j in range(0,len(result)-i):
                webj = lit_db.get_lit(result[j]['title'])
                webj1 = lit_db.get_lit(result[j+1]['title'])
                if webj is not None and webj1 is not None and webj['favorites']<webj1['favorites']:
                    result[j],result[j+1] = result[j+1],result[j]
                elif webj is None and webj1 is not None:
                    result[j], result[j + 1] = result[j + 1], result[j]
        dfav = dict()
        favlist = []
        lm1=[]
        fm1=[]
        for i in range(0,3):
            dfav[i] = result[i]
            web = lit_db.get_lit(result[i]['title'])
            if web is not None:
                favlist.append(web['favorites'])
            else:
                favlist.append(0)
            flaglike = False
            for j in range(len(likelist1)):
                if result[i]['link'] == likelist1[j]['link']:
                    lm1.append(1)
                    flaglike = True
                    break
            if not flaglike:
                lm1.append(0)
            flagfav = False
            for j in range(len(favlist1)):
                if result[i]['link'] == favlist1[j]['link']:
                    fm1.append(1)
                    flagfav = True
                    break
            if not flagfav:
                fm1.append(0)


        for i in range(1,len(result)):
            for j in range(0,len(result)-i):
                webj = lit_db.get_lit(result[j]['title'])
                webj1 = lit_db.get_lit(result[j+1]['title'])
                if webj is not None and webj1 is not None and webj['browses']<webj1['browses']:
                    result[j],result[j+1] = result[j+1],result[j]
                elif webj is None and webj1 is not None:
                    result[j], result[j + 1] = result[j + 1], result[j]
        dbr = dict()
        brlist = []
        lm2=[]
        fm2=[]
        for i in range(0, 3):
            dbr[i] = result[i]
            web = lit_db.get_lit(result[i]['title'])
            if web is not None:
                brlist.append(web['browses'])
            else:
                brlist.append(0)
            flaglike = False
            for j in range(len(likelist1)):
                if result[i]['link'] == likelist1[j]['link']:
                    lm2.append(1)
                    flaglike = True
                    break
            if not flaglike:
                lm2.append(0)
            flagfav = False
            for j in range(len(favlist1)):
                if result[i]['link'] == favlist1[j]['link']:
                    fm2.append(1)
                    flagfav = True
                    break
            if not flagfav:
                fm2.append(0)
        return render_template('literature_search_results.html', dic=d, query=query, search_type=search_type,
                                dlike=dlike,dbr=dbr,dfav=dfav, pn=pn,likelist=likelist,favlist=favlist,brlist=brlist,
                                likemask=likemask,favmask=favmask,lm=lm,fm=fm,lm1=lm1,fm1=fm1,lm2=lm2,fm2=fm2,
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
        web_like_db = database.get_web_like_database()
        time = datetime.datetime.now()
        time_now = str(time.year) + '.' + str(time.month) + '.' + str(time.day) + ',' + str(time.hour) + ':' + str(
            time.minute)
        web_like_db.add_web_like(username,title,url,time_now)
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
        web_like_db = database.get_literature_like_database()
        time = datetime.datetime.now()
        time_now = str(time.year) + '.' + str(time.month) + '.' + str(time.day) + ',' + str(time.hour) + ':' + str(
            time.minute)
        web_like_db.add_literature_like(username,title,url,time_now)
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
            web_db_item.update_web_item(web['id'], url, web['title'], web['origin'], web['snippet'], web['time_origin'],
                                   web['likes'], web['favorites'] + 1, web['browses'])
        time = datetime.datetime.now()
        time_now = str(time.year) + '.' + str(time.month) + '.' + str(time.day) + ',' + str(time.hour) + ':' + str(
            time.minute)
        web_db.add_web_favorite(username, title, url, time_now)
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
        lit_db.add_literature_favorite(username, title, url, time_now)
        return redirect(
            '/search_results?q=' + query + '&search_type=' + search_type + '&pn=' + pn + '&username=' + username)
