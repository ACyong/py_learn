import pymysql


class DBUtil:
    def __init__(self,**kwargs):
        #DBUtil(host='192.168.3.5',database='db')
        #完成对数据库的联接
        #kwargs字典 kwargs['host'],kwargs.get('port',3306)
        #host port user password database charset
        host = kwargs.get('host', '127.0.0.1')
        port = kwargs.get('port', 3306)
        user = kwargs.get('user', 'root')
        password = kwargs.get('password', '123')
        database = kwargs.get('database', 'blogdb')
        charset = kwargs.get('charset', 'utf8')

        settings={}
        settings['host']=host
        settings['port'] = port
        settings['user']=user
        settings['password'] = password
        settings['database'] = database
        settings['charset'] = charset
        conection = pymysql.connect(**settings)
        if conection:
            self.cursor = conection.cursor()
        else:
            raise Exception('数据库连接参数错误！')

    def saveuser(self,username,password,city,avatar):
        sql='insert into tb_user(user_name, user_password, user_avatar, user_city) VALUES (%s,%s,%s,%s)'
        params=(username,password,avatar,city)
        try:
            self.cursor.execute(sql,params)
            self.cursor.connection.commit()
        except Exception as e:
            print('错误信息：',e)
            info = 'dberror'
            code = str(e).split(',')[0].split('(')[1]
            if code=='1062':
                info = 'duplicate'
            raise Exception(info)

    def login(self,username,password):

        sql='select count(*) from tb_user where user_name=%s and user_password=%s'
        params=(username,password)
        self.cursor.execute(sql,params)
        result = self.cursor.fetchone()
        if result[0]:
            return True
        else:
            return False


    def getblogs(self):

        sql='''
            select blog_title,blog_content,gc,user_name,user_avatar,c

from (select comment_blog_id,count(*)c 

from tb_comment 

group by comment_blog_id)t3

right join (select blog_title,blog_content,gc,user_name,user_avatar,blog_id

from tb_user

join (select blog_title,blog_content,gc,blog_user_id,blog_id

from tb_blog

left join (select rel_blog_id,group_concat(tag_name)gc

from tb_tag

join tb_blog_tag

on rel_tag_id = tag_id

group by rel_blog_id)t

on rel_blog_id = blog_id)t2

on blog_user_id = user_id
)t4

on comment_blog_id = blog_id
        '''

        self.cursor.execute(sql)

        result = self.cursor.fetchall()
        #(('第一篇博客','xxxx' ,'抽烟,星座,爱情', 'ccc', None, 3),(...),(...))

        #[{'title':'第一篇博客','tags':'抽烟,星座,爱情'},{}]

        blogs=[]
        for b in result:
           blog={}
           blog['title']=b[0]
           blog['content']=b[1]
           if b[2]:
               blog['tags']=b[2]
           else:
               blog['tags']=''

           blog['author']=b[3]
           blog['avatar']=b[4]
           blog['comment']=b[5]
           blogs.append(blog)

        return blogs

    def checkname(self,username):

        sql='select count(*) from tb_user where user_name=%s'
        params=(username,)
        self.cursor.execute(sql,params)
        result = self.cursor.fetchone()#(1,)(0,)
        if result[0]:
            return True #有这个名字
        else:
            return False #没有这个名字

    def getavatar(self,username):
        sql='select user_avatar from tb_user where user_name=%s'
        params=(username,)
        self.cursor.execute(sql,params)
        #如果username是tb_user不存在的用户名
        #fetchone获得的result是None
        result = self.cursor.fetchone()
        if result:
            if result[0]:
                return result[0]
            else:
                return 'default_avatar.png'
        else:
            return 'default_avatar.png'
