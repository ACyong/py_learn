from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        # 获取自定义的请求头中的信息
        # h = self.request.headers
        # my = h['myhead']
        # you = h['youhead']
        # print(my)
        # print(you)

        msg = self.get_query_argument('msg', None)
        if msg:
            html = '''
            <form action='/login' method='post'>
                <span>用户名： </span><input type="text" name="username"><br>
                <span>密码： </span><input type="password" name="pwd"><br>
                <span>用户名或密码输入错误</span><br>
                <input type="submit" value="登陆">
                <input type="reset" value="重置">
            </form>
            '''
            self.write(html)
        else:
            html = '''
            <form action='/login' method='post' enctype=multipart/form-data>
                <span>用户名： </span><input type="text" name="username"><br>
                <span>密码： </span><input type="password" name="pwd"><br>
                <input type="file" name=avatar><br>
                <input type="file" name=avatar><br>
                <input type="submit" value="登陆">
                <input type="reset" value="重置">
            </form>
            '''
            self.write(html)


class LoginHandler(RequestHandler):

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        name = 'abc'
        password = '123'

        postname = self.get_body_argument('username', None)
        postpassword = self.get_body_argument('pwd', None)
        if name == postname and password == postpassword:
            # 如果用户上床了文件，则保存文件
            files = self.request.files
            if files:
                avatars = files['avatar']
                for avatar in avatars:
                    f_name = avatar['filename']
                    print('文件名：', f_name)
                    f_type = avatar['content_type']
                    print('文件类型：', f_type)
                    f_body = avatar['body']
                    writer = open('upload/{}'.format(f_name), 'wb')
                    # writer = open('upload/%s' % f_name, 'wb')
                    writer.write(f_body)
                    writer.close()

            # self.write('登陆成功！')
            self.redirect('/blog/?name=' + name)
        else:
            # self.write('失败！')
            self.redirect('/?msg=fail')


class BlogHandler(RequestHandler):

    def get(self, *args, **kwargs):
        name = self.get_query_argument('name', None)
        if name:
            self.write('欢迎来到' + name + 'blog 页面')
        else:
            self.write('欢迎来到blog 页面')

    def post(self, *args, **kwargs):
        pass


# 1 定义一个代表端口号的变量名称
define('port', type=int, default=8888)
define('db', type=str, default=[], multiple=True)

# 2 解析配置文件
parse_config_file('../config/config')
app = Application([('/', IndexHandler),
                   ('/login', LoginHandler),
                   ('/blog/', BlogHandler),
                   ])

server = HTTPServer(app)
server.listen(options.port)  # 3 读取配置文件中的端口号
IOLoop.current().start()
