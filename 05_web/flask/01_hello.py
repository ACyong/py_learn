# -*- coding: utf-8 -*-

from flask import Flask

# 1.这个类的实例将会 WSGI 应用程序
app = Flask(__name__)


@app.route('/')
def index():
    """2.route() 装饰器把一个视图函数绑定到对应的 URL 上，
    视图函数就是MVC中的 controller
    """
    return 'Hello World!'


@app.route('/decorator')
def decorator():
    """3.路由设置成'/decorator/'将兼容'/decorator'和'/decorator/'两种URL，这种情况
    '/decorator'实际上是做了一次重定向
    """
    return 'Hello Decorator!'


def class_view():
    """6.推荐使用装饰器来设置URL，如果想实现基于类的视图（即插视图），
    可以使用app这个实例来实现
    """
    return 'Hello ClassView!'


app.add_url_rule('/class_view', view_func=class_view)

if __name__ == '__main__':
    # 4.run() 函数来让应用运行在本地服务器上
    app.run()
    # 使服务器公开
    app.run(host='0.0.0.0')

    # 5.调试模式两种方法
    # (1)
    app.debug = True
    app.run()
    # (2)
    app.run(debug=True)
