from flask import Flask
from .views.auth_ctrl import auth_ctrl
from .views.index_ctrl import index_ctrl
from .views.manage_ctrl import manage_ctrl
from .views.result_ctrl import result_ctrl
from .views.relation_ctrl import relation_ctrl
from .views.summary_ctrl import summary_ctrl

def create_app():
# 创建 Flask 应用实例
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ayuwhefgeawhfaweb123i4123dahu3iwhwq'
    app.config['SESSION_TYPE'] = 'redis'
    
    # @app.route('/')

    # 注册蓝图
    app.register_blueprint(auth_ctrl)
    app.register_blueprint(index_ctrl)
    app.register_blueprint(manage_ctrl)
    app.register_blueprint(result_ctrl)
    app.register_blueprint(relation_ctrl)
    app.register_blueprint(summary_ctrl)
    
    return app


