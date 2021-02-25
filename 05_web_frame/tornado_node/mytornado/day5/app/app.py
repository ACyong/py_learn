from tornado.web import Application

from day5.app import mysettings
from day5.util.dbutil import DBUtil


class MyApplication(Application):
    def __init__(self,handlers,tp,sp,ui):

        super().__init__(handlers,
                         template_path=tp,
                         static_path=sp,
                         ui_modules=ui)

        self.dbutil=DBUtil(**mysettings.settings['dbsetting'])
