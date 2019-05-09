# -*- coding: utf-8 -*-

from flask import Flask, make_response


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    """1.视图函数的return与普通函数的return是不一样的，主要区别在与返回值
    视图函数会返回一个response对象，主要包括状态码status-code：200，301，404，503...，
    content-type（包含在HTTP header中）等,如果不指定content-type，默认返回为text/html
    """
    headers = {
        'content-type': 'text/plain',  # 普通文本格式
        'location': 'http://www.baidu.com'
    }
    # 状态码只是一个标识，并不会对显示内容有影响
    response = make_response('<html></html>', 301)
    response.headers = headers
    return response


@app.route('/return')
def return_response():
    headers = {
        'content-type': 'text/plain',  # json格式 'application/json'
    }

    # 2.这种返回response对象的格式更常用、简洁，
    return '<html>return</html>', 404, headers


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=10001)
