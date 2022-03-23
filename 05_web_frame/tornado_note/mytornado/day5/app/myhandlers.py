from random import randint

import time

from os import remove
from tornado.web import RequestHandler

from day5.util.myutil import mymd5
from day5.util.session import MySession


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #服务器向浏览器写入cookie
        session = MySession(self)
        if session['islogin']:
            self.redirect('/blog')
        else:
            self.render('login.html')

    def post(self, *args, **kwargs):
        pass

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        username = self.get_body_argument('uname')
        password = self.get_body_argument('password')
        print('username:',username,' password:',password)
        #MyApplication中的dbutil属性所引用的那个DBUtil对象

        if self.application.dbutil.login(username=username,password=mymd5(password)):

            session = MySession(self)
            session['islogin']=True
            session['username']=username
            self.redirect('/blog')
        else:
            self.redirect('/?msg=fail')


class BlogHandler(RequestHandler):

    def myrand(self,a,b):
        return randint(a,b)#[15,40]

    def set_default_headers(self):
        print('set_default_headers方法被执行')
        #作者设计该钩子方法的目的是：
        #希望程序员在这里设置响应内容的默认响应头
        self.set_header('tedu','aid1712')

    def initialize(self,date,subject):
        print('initialize方法被执行')
        # 作者设计该钩子方法的目的是：
        # 接受程序员在构建该路由时从路由列表传入的参数
        self.date = date
        self.subject = subject


    def on_finish(self):
        print('on_finish方法被执行')
        # 作者设计该钩子方法的目的是：
        # 在响应内容已经生成后，可以在这里释放一些资源

    def get(self, *args, **kwargs):

        session = MySession(self)
        if session['islogin']:
            self.render('blog.html')
        else:
            self.redirect('/')

    def post(self, *args, **kwargs):
        pass

    def write_error(self, status_code, **kwargs):
        if status_code == 200:

            err='<span style=color:red;font-size:48px;font-weight:bolder;>这是一个极其恐怖的错误！</span>'

            self.write(err)
        else:
            #应该继续执行父类方法中原有的逻辑
            super().write_error(status_code, **kwargs)

class RegistHandler(RequestHandler):
    def get(self, *args, **kwargs):

        result = self.get_cookie('mycookie')
        print('mycookie值是：',result)

        self.render('regist.html')
    def post(self, *args, **kwargs):
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        city = self.get_body_argument('city')
        avatar=None
        print(username,password,city)

        if username and password and city:

           if self.request.files:
               file = self.request.files['avatar'][0]
               #把用户上传的头像文件保存到服务器磁盘
               path = str(time.time())+file['filename']
               writer = open('mystatics/images/{}'.format(path),'wb')
               writer.write(file['body'])
               writer.close()
               avatar = path


           try:
                self.application.dbutil.saveuser(username=username,password=mymd5(password),avatar=avatar,city=city)
           except Exception as e:
                if avatar:
                    remove('mystatics/images/'+avatar)
                info = str(e)#'dberror''duplicate'
                self.redirect('/regist?msg='+info)
           else:
                self.redirect('/')


        else:
            self.redirect('/regist?msg=empty')


class CheckHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):

        type = self.get_body_argument("type")

        if type=='regist':

            username = self.get_body_argument('username')
            if self.application.dbutil.checkname(username):
                #返回一个信息，告诉用户该名字不能被使用
                self.write({'msg':'fail'})
            else:
                #返回一个信息，告诉用户该名字能被使用
                self.write({'msg':'ok'})

        if type=='login':
            username = self.get_body_argument('username')
            result = self.application.dbutil.getavatar(username)
            self.write({'msg':result})
