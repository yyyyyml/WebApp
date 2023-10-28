from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database
from summary import get_summary
import os  # 导入 os 模块
import mistune
import markdown2


summary_ctrl = Blueprint('summary_ctrl', __name__)

@summary_ctrl.route('/summary')
def summary():
    # 获取文献的 URL 参数
    url = request.args.get('url')

    # 调用 get_summary 函数生成总结文档，得到总结 md 文档的路径
    summary_path = get_summary(url)

    # 读取 md 文件的内容
    summary_content = ""
    if os.path.exists(summary_path):
        with open(summary_path, 'r', encoding='utf-8') as file:
            summary_content = file.read()

    # markdown = mistune.Markdown()
    html_content = markdown2.markdown(summary_content)

    return render_template('summary.html', local_pdf_path='E:\Py_Code\WebApp\papers\Boosting the Throughput and Accelerator Utilization of Specialized CNN Inference Beyond Increasing Batch Size.pdf', summary_content=html_content)

# 现在先不需要这个
@summary_ctrl.route('/proxy_page')
def proxy_page():
    document_url = request.args.get('document_url')
    return render_template('summary_proxy.html', document_url=document_url)