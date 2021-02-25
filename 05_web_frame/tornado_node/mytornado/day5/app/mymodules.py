from tornado.web import UIModule


class LoginModule(UIModule):
    def render(self, *args, **kwargs):

        m = ''
        #print('uri:',self.request.uri)#path + query
        #print('path:',self.request.path)#请求路径
        #print('query:',self.request.query)#get方式请求参数
        if self.request.query:
            m = '用户名或密码错误！'

        return self.render_string('mymodule/login_module.html',result=m)

class BlogModule(UIModule):
    def render(self, *args, **kwargs):


        blogs = self.handler.application.dbutil.getblogs()

        return self.render_string('mymodule/blog_module.html',blogs=blogs)

class RegistModule(UIModule):
    def render(self, *args, **kwargs):

        m=''
        #根据msg的不同信息，生成不同的m内容
        #empty：注册信息不完整
        #duplicate:用户名充分
        #dberror:数据库错误
        if self.request.query:
            #msg=empty
            q = self.request.query.split('=')[1]
            if q=='empty':
                m='注册信息不完整'
            if q=='duplicate':
                m='用户名重复'
            if q=='dberror':
                m='数据库错误，稍后重试'

        return self.render_string('mymodule/regist_module.html',result=m)

