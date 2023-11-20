import time
from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash, session, send_from_directory, copy_current_request_context
from flask.ctx import RequestContext
import requests
from database import get_user_database, get_literature_item_database
from summary import get_summary, get_summary_filename
import os  # 导入 os 模块
import mistune
import markdown2
from threading import Thread

summary_ctrl = Blueprint('summary_ctrl', __name__)

@summary_ctrl.route('/summary')
def summary():
    # 获取文献的 URL 参数
    url = request.args.get('url')
    pdf_path = request.args.get('pdf_path')
    username = request.args.get('username')
    pdf_filename = request.args.get('pdf_filename')
    
    print(url)
    
    if pdf_path is None:
        # 将 URL 进行处理以作为文件名
        paper_filename = url.replace('/', '_').replace(':', '_')
        # 检查文件是否已存在，如果存在则不重新写入
        pdf_path = os.path.join('papers', paper_filename)
    else:
        url = pdf_path
        paper_filename = pdf_filename

    if not os.path.exists(pdf_path):
        response = requests.get(url)
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(response.content)

    # 使用数据库操作获取 summary_filename
    literature_item_db = get_literature_item_database()
    db_summary_filename = literature_item_db.get_summary_path(url)

    if db_summary_filename is None:
        summary_filename = get_summary_filename(pdf_path)
        def generate_summary():
            nonlocal db_summary_filename
            nonlocal summary_filename
            if db_summary_filename is None:
                # 如果 db_summary_filename 不存在，调用 get_summary 函数生成总结文档
                
                # 使用数据库操作添加或更新 summary_path
                literature_item_db = get_literature_item_database()
                literature_item_db.add_or_update_summary_path(url, get_summary(pdf_path, summary_filename))

        summary_thread = Thread(target=generate_summary)
        summary_thread.start()
        
        
        # return redirect(url_for('summary_ctrl.loading1', paper_filename=paper_filename, summary_path=summary_path))
        print(summary_filename)
        return render_template('summary.html', paper_filename=paper_filename, summary_content="正在总结中...", summary_filename=summary_filename, username=username)
    else: 
        summary_path = os.path.join('summary', db_summary_filename)
        # summary_path = db_summary_filename
        # 读取 md 文件的内容
        summary_content = ""
        if os.path.exists(summary_path):
            with open(summary_path, 'r', encoding='utf-8') as file:
                summary_content = file.read()

        html_content = markdown2.markdown(summary_content)

        return render_template('summary.html', paper_filename=paper_filename, summary_content=html_content, username=username)


@summary_ctrl.route('/check_summary')
def check_summary():
    summary_filename = request.args.get('summary_filename')
    summary_path = os.path.join('summary', summary_filename)

    if os.path.exists(summary_path):
        # 总结已生成，返回总结内容
        with open(summary_path, 'r', encoding='utf-8') as file:
            summary_content = file.read()
        html_content = markdown2.markdown(summary_content)
        return jsonify({"generated": True, "summary_content": html_content})
    else:
        # 总结未生成完毕
        return jsonify({"generated": False})
    

@summary_ctrl.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    username = request.args.get('username')
    if 'pdf_file' in request.files:
        pdf_file = request.files['pdf_file']
        if pdf_file.filename != '':
            # Generate a unique filename for the uploaded file
            pdf_filename = pdf_file.filename
            pdf_path = os.path.join('papers', pdf_filename)
            pdf_file.save(pdf_path)

            # Pass the file path to the summary page
            return redirect(url_for('summary_ctrl.summary', pdf_path=pdf_path, pdf_filename=pdf_filename, username=username))

    return redirect(url_for('summary_ctrl.summary'))

@summary_ctrl.route('/pdf/<filename>')
def pdf(filename):
    pdf_directory = '../papers'
    return send_from_directory(pdf_directory, filename)

# 现在先不需要这个
@summary_ctrl.route('/proxy_page')
def proxy_page():
    document_url = request.args.get('document_url')
    return render_template('summary_proxy.html', document_url=document_url)