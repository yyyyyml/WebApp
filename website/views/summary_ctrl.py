from flask import Blueprint, render_template, request, redirect, url_for, flash, session, send_from_directory
import requests
from database import get_user_database, get_literature_item_database
from summary import get_summary
import os  # 导入 os 模块
import mistune
import markdown2


summary_ctrl = Blueprint('summary_ctrl', __name__)

@summary_ctrl.route('/summary')
def summary():
    # 获取文献的 URL 参数
    url = request.args.get('url')

    # 将 URL 进行处理以作为文件名
    paper_filename = url.replace('/', '_').replace(':', '_').replace('?', '_')

    # 检查文件是否已存在，如果存在则不重新写入
    pdf_path = os.path.join('papers', paper_filename)
    if not os.path.exists(pdf_path):
        response = requests.get(url)
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(response.content)

    # 使用数据库操作获取 summary_path
    literature_item_db = get_literature_item_database()
    summary_path = literature_item_db.get_summary_path(url)

    if summary_path is None:
        # 如果 summary_path 不存在，调用 get_summary 函数生成总结文档
        summary_path = get_summary(pdf_path)
        # 使用数据库操作添加或更新 summary_path
        literature_item_db.add_or_update_summary_path(url, summary_path)

    # 读取 md 文件的内容
    summary_content = ""
    if os.path.exists(summary_path):
        with open(summary_path, 'r', encoding='utf-8') as file:
            summary_content = file.read()

    html_content = markdown2.markdown(summary_content)

    return render_template('summary.html', paper_filename=paper_filename, summary_content=html_content)




@summary_ctrl.route('/pdf/<filename>')
def pdf(filename):
    pdf_directory = '../papers'
    return send_from_directory(pdf_directory, filename)

# 现在先不需要这个
@summary_ctrl.route('/proxy_page')
def proxy_page():
    document_url = request.args.get('document_url')
    return render_template('summary_proxy.html', document_url=document_url)