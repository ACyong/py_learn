# escape 转义
from http.server import HTTPServer
from tornado import options
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.render('escape.html', result='')

    def post(self, *args, **kwargs):
        m = self.get_query_argument('txt', None)
        self.render('escape.html', result=m)


app = Application([('/', IndexHandler),],
                  template_path='mytemplate',
                  autoreload=None,
                  )

server = HTTPServer(app)
server.listen(options.port)  # 3 读取配置文件中的端口号
IOLoop.current().start()