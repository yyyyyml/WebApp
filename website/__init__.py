from flask import Flask
from .views.auth import auth
from .views.home import home

def create_app():
# 创建 Flask 应用实例
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ayuwhefgeawhfaweb123i4123dahu3iwhwq'
    
    # @app.route('/')

    # 注册蓝图
    app.register_blueprint(auth)
    app.register_blueprint(home)
    
    return app


