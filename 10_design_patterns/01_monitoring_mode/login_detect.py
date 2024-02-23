import time

from observable import Observable
from observer import Observer


class Account(Observable):
    def __init__(self):
        super().__init__()
        self.__latest_ip = {}
        self.__latest_region = {}

    def login(self, name, ip, login_time):
        region = self.__get_region(ip)
        if self.__is_long_distance(name, region):
            self.notify_observers({'name': name, 'ip': ip, 'region': region, 'login_time': login_time})
        self.__latest_ip[name] = ip
        self.__latest_region[name] = region

    @staticmethod
    def __get_region(ip):
        """通过 ip 获取地区"""
        ip_region = {
            "101.47.18.9": "北京",
            "67.218.147.69": "美国",
        }
        return ip_region.get(ip, "未知")

    def __is_long_distance(self, name, region):
        latest_region = self.__latest_region.get(name)
        return latest_region is not None and latest_region != region


class SmsSender(Observer):
    def update(self, observable, obj):
        print(f'[短信发送] {obj["name"]} 异地登录，登录地点：{obj["region"]}，登录ip：{obj["ip"]}，'
              f'登录时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(obj["login_time"]))}')


class MailSender(Observer):
    def update(self, observable, obj):
        print(f'[邮件发送] {obj["name"]} 异地登录，登录地点：{obj["region"]}，登录ip：{obj["ip"]}，'
              f'登录时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(obj["login_time"]))}')


if __name__ == '__main__':
    account = Account()
    account.add_observer(SmsSender())
    account.add_observer(MailSender())
    account.login('张三', '101.47.18.9', time.time())
    account.login('张三', '67.218.147.69', time.time())
