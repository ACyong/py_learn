import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import define, options
from tornado.web import RequestHandler, url


define('port', type=int, default=8000, help='服务器端口')


class IndexHandler(RequestHandler):
    """主页处理类"""

    def get(self):
        """get 请求"""
        self.write('<a href="' + self.reverse_url("cpp_url") + '">cpp</a>')


class SubjectHandler(RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [(r'/', IndexHandler),
         (r'/python', SubjectHandler, {'subject': 'python'}),
         url(r'/cpp', SubjectHandler, {'subject': 'cpp'}, name='cpp_url'), ],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
