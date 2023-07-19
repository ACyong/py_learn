
#{'6f2610266c159b4a2b6d9c649a7319ec':{'islogin':True}}
from day5.util.myutil import myuuid

session={}

class MySession:
    def __init__(self,handler):
       self.handler = handler

    def __getitem__(self, key):
        #6f2610266c159b4a2b6d9c649a7319ec
        cookieid = self.handler.get_cookie('mycookie')
        if cookieid:
            info = session.get(cookieid,None)
            if info:
                result = info.get(key,None)
                return result
            else:
                return None
        else:
            return None


    def __setitem__(self, key, value):
        cookieid = self.handler.get_cookie('mycookie')

        if cookieid:
            info = session.get(cookieid,None)
            if info:
                info[key] = value
            else:
                r = {}
                r[key]=value
                session[cookieid] = r
        else:
            r = {}
            r[key] = value
            cookieid = myuuid()
            session[cookieid] = r
            self.handler.set_cookie('mycookie',cookieid,expires_days=10)







