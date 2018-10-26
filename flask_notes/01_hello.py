# -*- coding: utf-8 -*-

from flask import Flask


# 1.这个类的实例将会 WSGI 应用程序
app = Flask(__name__)


# 2.route() 装饰器把一个视图函数绑定到对应的 URL 上，视图函数就是MVC中的controlor
@app.route('/')
def index():
    return 'Hello World!'


# 3.路由设置成'/decorator/'将兼容'/decorator'和'/decorator/'两种URL，'/decorator'实际上是做了一次重定向
@app.route('/decorator')
def decorator():
    return 'Hello Decorator!'


# 6.推荐使用装饰器来设置URL，如果想实现基于类的视图（即插视图）可以使用app这个实例来实现
def class_view():
    return 'Hello ClassView!'
app.add_url_rule('/class_view', view_func=class_view)


if __name__ == '__main__':
    # 4.run() 函数来让应用运行在本地服务器上
    # app.run()
    # 使服务器公开
    # app.run(host='0.0.0.0')

    # 5.调试模式两种方法
    # (1)
    # app.debug = True
    # app.run()
    # (2)
    app.run(debug=True)
