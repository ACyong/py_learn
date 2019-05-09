# -*- coding: utf-8 -*-

from flask import Flask, url_for


app = Flask(__name__)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login_form()


# 6.指定一个可选的转换器
# int     接受整数
# float   同 int ，但是接受浮点数
# path    和默认的相似，但也接受斜线
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/geturl/<path:url>')
def geturl(url):
    return url


# 7.反向构建通常比硬编码的描述性更好。更重要的是，它允许你一次性修改 URL， 而不是到处边找边改。
# URL 构建会转义特殊字符和 Unicode 数据，免去你很多麻烦。
# 如果你的应用不位于 URL 的根路径（比如，在 /myapplication 下，而不 是 / ）， url_for() 会妥善处理这个问题。
with app.test_request_context():
    print(url_for('index'))
    # print(url_for('login'))
    # print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='John Doe'))


if __name__ == '__main__':
    app.run(debug=True)
