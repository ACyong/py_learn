from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):

    # get_query_argument 和get_query_arguments 区别
    # 1、如果出现同名请求参数时，get_query_argument 只能保留最后一个
    #    get_query_arguments 以列表形式保留所有值
    # 2、使用get_query_argument 取请求参数时，最好提供默认值，防止用户未使用要求的参数导致程序报错
    #    使用get_query_arguments 时如果用户未使用要求的参数，只会返回一个空列表，但不会报错
    def get(self, *args, **kwargs):
        name = self.get_query_argument('username', None)
        pwd = self.get_query_argument('password', None)
        names = self.get_query_arguments('username')
        pwds = self.get_query_arguments('password')

        print('用户名：', name)
        print('密码：', pwd)
        print('names: ', names)
        print('pwds: ', pwds)

    def post(self, *args, **kwargs):
        name = self.get_body_argument('username', None)
        pwd = self.get_body_argument('password', None)
        names = self.get_body_arguments('username')
        pwds = self.get_body_arguments('password')

        arg = self.get_argument('key1', None)
        args = self.get_arguments('key1')

        print('用户名：', name)
        print('密码：', pwd)
        print('names: ', names)
        print('pwds: ', pwds)

        print('arg', arg)
        print('args', args)


# 1 定义一个代表端口号的变量名称
define('port', type=int, default=8888)
define('db', type=str, default=[], multiple=True)
# 2 解析配置文件
parse_config_file('../config/config')

app = Application([('/', IndexHandler)])

server = HTTPServer(app)
server.listen(options.port)  # 3 读取配置文件中的端口号
# print('数据库配置', options.db)
IOLoop.current().start()
