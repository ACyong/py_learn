from functools import wraps


class Singleton1:
    __instance = None
    __is_first_init = False

    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__is_first_init:
            self.__name = name
            self.__is_first_init = True

    def get_name(self):
        return self.__name


def test_singleton1():
    s1 = Singleton1('s1')
    s2 = Singleton1('s2')
    print(s1.get_name(), s2.get_name())
    print("id(s1):", id(s1), "id(s2):", id(s2))


class Singleton2(type):

    def __init__(cls, what, bases=None, _dict=None):
        super().__init__(what, bases, _dict)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class CustomSingleton(metaclass=Singleton2):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


def test_singleton2():
    s1 = CustomSingleton('s1')
    s2 = CustomSingleton('s2')
    print(s1.get_name(), s2.get_name())
    print("id(s1):", id(s1), "id(s2):", id(s2))


def singleton(cls):
    instances = {}

    @wraps(cls)
    def __singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return __singleton


@singleton
class Singleton3:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


def test_singleton3():
    s1 = Singleton3('s1')
    s2 = Singleton3('s2')
    print(s1.get_name(), s2.get_name())
    print("id(s1):", id(s1), "id(s2):", id(s2))


if __name__ == '__main__':
    test_singleton1()
    test_singleton2()
    test_singleton3()
