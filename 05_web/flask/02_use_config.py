# -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__)
# 2.使用配置文件，app.config.from_object(模块名)，配置文件中必须保证全部的参数都要大写
app.config.from_object('config')


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    # 1.完整的run函数的参数为：设置主机IP，开启调试模式，更换端口号
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=10001)
