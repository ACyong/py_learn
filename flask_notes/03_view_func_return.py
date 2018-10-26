# -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    # 视图函数的return与普通函数的return是不一样的，主要区别在与返回值
    # 视图函数会返回状态码status-code：200，301，404，503等，含有包含在HTTP header中的content-type
    # 如果不指定content-type，默认返回为text/html
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=10001)
