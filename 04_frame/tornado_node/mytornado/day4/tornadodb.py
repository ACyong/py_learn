import pymysql
import time
from os import remove
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, UIModule

from day4.util.dbutil import DBUtil
from day4.util.myutil import mymd5


class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        pass


class RegisterHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.render('register.html')

    def post(self, *args, **kwargs):
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        city = self.get_body_argument('city')
        avatar = None

        if username and password and city:
            if self.request.files:
                file = self.request.files['avatar'][0]
                # 把用户上传的头像文件保存到服务器磁盘上
                path = str(time.time()) + file['filename']
                writer = open('mystatics/images/{}'.format(path), 'wb')
                writer.write(file['body'])
                writer.close()
                avatar = path

            # settings = {'host': '127.0.0.1',
            #             'port': 3306,
            #             'user': 'root',
            #             'password': '123',
            #             'database': 'blogdb',
            #             'charset': 'utf8'
            #             }
            # connection = pymysql.connect(**settings)
            # cursor = connection.cursor()
            # sql = 'insert into tb_user(user_name, user_password, user_city, user_avatar) VALUES (%s, %s, %s, %s)'
            # pwd = mymd5(password)
            # params = (username, pwd, city, avatar)
            # # print('sql 语句：', sql)
            # try:
            #     cursor.execute(sql, params)
            #     cursor.connection.commit()
            # except Exception as e:
            #     # 发生错误将用户的头像删除
            #     if avatar:
            #         remove('mystatics/images/'+avatar)
            #     # 异常信息！ (1062, "Duplicate entry 'abc' for key 'user_name'")
            #     info = 'dberror'
            #     code = str(e).split(',')[0].split('(')[1]
            #     # 根据错误编码生成有用信息，将信息以参数的形式带回到注册页面
            #     # 例如：错误编码是1062，生成错误信息duplicate
            #     if code == '1062':
            #         info = 'duplicate'
            #     # print('异常信息！', e)
            #     self.redirect('/register?msg=' + info)
            # else:
            #     self.redirect('/')

            dbutil = DBUtil()
            try:
                dbutil.saveuser(username=username, password=mymd5(password), city=city, avatar=avatar)
            except Exception as e:
                info = str(e)  # 'dberror'\'duplicate'
                self.redirect('/register?msg='+info)
            else:
                self.redirect('/')

        else:
            self.redirect('/register?msg=empty')


class LoginHandler(RequestHandler):

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        # username = self.get_body_argument('username', None)
        # password = self.get_body_argument('password', None)

        # 1、建立与数据库的连接
        # settings = {'host': '127.0.0.1',
        #             'port': 3306,
        #             'user': 'root',
        #             'password': '123',
        #             'database': 'blogdb',
        #             'charset': 'utf8'
        #             }
        # connection = pymysql.connect(**settings)
        # 2、获取游标
        # cursor = connection.cursor()
        # 3、利用游标发送SQL 语句
        # sql = 'select count(*) from tb_user WHERE user_name="{}" AND user_password="{}"'.format(username, password)
        # 上面的方法容易遭到sql 攻击
        # sql = 'select count(*) from tb_user WHERE user_name=%s AND user_password=%s'
        # pwd = mymd5(password)
        # params=(username, pwd)
        # print('sql 语句：', sql)
        # cursor.execute(sql, params)
        # 4、利用游标获取结果
        # result = cursor.fetchall()
        # result = cursor.fetchone()
        # print('执行结果：', result)
        # 5、根据result 决定跳转方向
        # if result[0]:
        #     self.redirect('/blog')
        # else:
        #     self.redirect('/?msg=fail')
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        print('username:', username, ' password:', password)
        dbutil = DBUtil()
        if dbutil.login(username=username, password=mymd5(password)):
            self.redirect('/blog')
        else:
            self.redirect('/?msg=fail')


class BlogHandler(RequestHandler):

    def get(self, *args, **kwargs):
        # self.render('blog.html', a=15, b=40, rand=self.myrand)
        self.render('blog.html')

    def post(self, *args, **kwargs):
        pass

    def write_error(self, status_code, **kwargs):
        if status_code == 200:
            err = '这是一个错误'
            self.write(err)
        else:
            # 应该继续执行父类的原有逻辑
            super().write_error(status_code, **kwargs)


class LoginModule(UIModule):

    def render(self, *args, **kwargs):
        m = ''
        if self.request.query:
            m = '用户名或密码错误'
        return self.render_string('mymodule/login_module.html', result=m)


class RegisterModule(UIModule):

    def render(self, *args, **kwargs):
        m = ''
        # 根据msg 的不同信息，生成不同的m 内容
        # empty：注册信息不完整
        # duplicate：用户名重复
        # dberror：数据库错误
        if self.request.query:
            q = self.request.query.split('=')[1]
            if q == 'empty':
                m = '注册信息不完整'
            if q == 'duplicate':
                m = '用户名重复'
            if q == 'dberror':
                m = '服务器繁忙'
        return self.render_string('mymodule/register_module.html', result=m)


class BlogModule(UIModule):
    # def render(self, *args, **kwargs):
    #     return self.render_string('mymodule/blog_module.html', blogs=[
    #                             {'author': '大虚',
    #                              'avatar': 'a.jpg',
    #                              'title': '办证',
    #                              'tags': '情感 家庭 星座',
    #                              'content': '嘻嘻嘻嘻嘻嘻',
    #                              'comment': 3},
    #                             {
    #                              'author': '小虚',
    #                              'avatar': None,
    #                              'title': '办证',
    #                              'tags': '情感 家庭 星座',
    #                              'content': 'hhh嘻嘻嘻',
    #                              'comment': 8},
    #                             {
    #                              'author': '小小虚',
    #                              'avatar': 'a.jpg',
    #                              'title': '办证',
    #                              'tags': '情感 家庭 星座',
    #                              'content': 'hhh嘻嘻嘻',
    #                              'comment': 0},
    #                             ])
    def render(self, *args, **kwargs):
        dbutil = DBUtil()
        blogs = dbutil.getblogs()

        return self.render_string('mymodule/blog_module.html', blogs=blogs)


# 1 定义一个代表端口号的变量名称
define('port', type=int, default=8888)
define('db', type=str, default=[], multiple=True)

# 2 解析配置文件
parse_config_file('../config/config')
app = Application([('/', IndexHandler),
                   ('/login', LoginHandler),
                   ('/blog', BlogHandler),
                   ('/register', RegisterHandler), ],
                  template_path='mytemplate',
                  static_path='mystatics',
                  ui_modules={'loginmodule': LoginModule,
                              'blogmodule': BlogModule,
                              'registermodule': RegisterModule,
                             }
                  )

server = HTTPServer(app)
server.listen(options.port)  # 3 读取配置文件中的端口号
IOLoop.current().start()
