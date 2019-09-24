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

    def set_default_headers(self):
        print('set_defualt_header 被执行了')
        # 作者设计该钩子方法的目的是：希望程序员在这里设置响应内容的默认响应头
        self.set_header('zyz', '123')

    def initialize(self, data, subject):
        print('initialize 方法被执行')
        # 作者设计该钩子方法的目的是：希望程序员在构建该路由时从路由列表中传入的参数
        self.data = data
        self.subject = subject

    def on_finish(self):
        print('on_finish 方法被执行了')
        # 作者设计该钩子方法的目的是：在响应内容已经生成后，可以在这里释放一些资源

    def get(self, *args, **kwargs):
        name = self.get_query_argument('name', None)
        if name:
            self.write('欢迎来到' + name + 'blog 页面')
            # self.set_status(404)
            # 手动设置状态码
            # ValueError：unknown status code 808
            self.set_status(808, 'funny status code')
            # 手动抛出一个错误，默认错误代码为500
            self.send_error()
            # self.send_error(200)
        else:
            self.write('欢迎来到blog 页面')

    def post(self, *args, **kwargs):
        pass

    def write_error(self, status_code, **kwargs):
        if status_code == 200:
            err = '这是一个错误'
            self.write(err)
        else:
            # 应该继续执行父类的原有逻辑
            super().write_error(status_code, **kwargs)


# 1 定义一个代表端口号的变量名称
define('port', type=int, default=8888)
define('db', type=str, default=[], multiple=True)

# 2 解析配置文件
parse_config_file('../config/config')
app = Application([('/', IndexHandler),
                   ('/login', LoginHandler),
                   ('/blog/', BlogHandler, {'data': '0408', 'subject': 'tornado'}),
                   ])

server = HTTPServer(app)
server.listen(options.port)  # 3 读取配置文件中的端口号
IOLoop.current().start()
