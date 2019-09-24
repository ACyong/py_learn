from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.write('Hello tornado')

    def post(self, *args, **kwargs):
        pass


class PythonHandler(RequestHandler):

    def get(self, day=None, subjuect=None, *args, **kwargs):
        if day:
            self.write('day: ' + day)
        if subjuect:
            self.write('课程：' + subjuect)
        self.write('hello python')

    def post(self, *args, **kwargs):
        pass


class JavaHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.write('hello Java')

    def post(self, *args, **kwargs):
        pass


# 1 定义一个代表端口号的变量名称
define('port', type=int, default=8888)
define('db', type=str, default=[], multiple=True)
# 2 解析配置文件
parse_config_file('../config/config')

app = Application([('/', IndexHandler),
                   ('/python', PythonHandler),
                   ('/java', JavaHandler),
                   ('/python/(day[0-9]+)', PythonHandler),
                   ('/python/(day[0-9]+)/([a-zA-Z0-9]+)', PythonHandler)
                   ])

server = HTTPServer(app)
server.listen(options.port)  # 3 读取配置文件中的端口号
# print('数据库配置', options.db)
IOLoop.current().start()
