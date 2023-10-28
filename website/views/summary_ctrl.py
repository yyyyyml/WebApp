from flask import Blueprint, redirect, render_template, request, flash, send_from_directory
from summary import get_summary

summary_ctrl = Blueprint('summary_ctrl', __name__)

@summary_ctrl.route('/summary', methods=['GET', 'POST'])
def summary():
    if request.method == 'POST':
        # 检查是否有文件上传
        if 'literature' not in request.files:
            flash('没有选择文件', 'error')
            return redirect(request.url)

        literature = request.files['literature']

        # 检查文件是否为空
        if literature.filename == '':
            flash('文件名不能为空', 'error')
            return redirect(request.url)

        if literature:
            # 保存文献文件
            literature.save('uploads/' + literature.filename)

            # 调用函数生成总结
            summary_path = get_summary('uploads/' + literature.filename)

            # 读取文献内容
            with open('uploads/' + literature.filename, 'r') as lit_file:
                literature_content = lit_file.read()

            # 读取总结内容
            with open(summary_path, 'r') as summary_file:
                summary_content = summary_file.read()

            return render_template('summary.html', literature_content=literature_content, summary_content=summary_content)

    return render_template('summary.html', literature_content=None, summary_content=None)
