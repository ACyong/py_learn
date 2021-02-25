from random import randint

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler
import json


class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        m = ''  # 用户名或密码
        if self.get_query_argument('msg', None):
            m = '用户名或密码错误'
        self.render('login.html', result=m)

    def post(self, *args, **kwargs):
        pass


class LoginHandler(RequestHandler):

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        name = 'abc'
        password = '123'

        postname = self.get_body_argument('username', None)
        postpassword = self.get_body_argument('password', None)
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

    def myrand(self, a, b):
        return randint(a, b)

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
        # self.render('blog.html', a=15, b=40, rand=self.myrand)
        self.render('blogfor.html', blogs=[{'author': '大虚',
                                            'title': '办证',
                                            'tags': '情感 家庭 星座',
                                            'content': '嘻嘻嘻嘻嘻嘻',
                                            'comment': 3},
                                           {
                                            'author': '小虚',
                                            'title': '办证',
                                            'tags': '情感 家庭 星座',
                                            'content': 'hhh嘻嘻嘻',
                                            'comment': 8},
                                           {
                                            'author': '小小虚',
                                            'title': '办证',
                                            'tags': '情感 家庭 星座',
                                            'content': 'hhh嘻嘻嘻',
                                            'comment': 0},
                                           ])

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
                   ], template_path='mytemplate')

server = HTTPServer(app)
server.listen(options.port)  # 3 读取配置文件中的端口号
IOLoop.current().start()
