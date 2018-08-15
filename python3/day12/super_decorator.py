"""给不同的函数加上同一个装饰器，赋予不同的功能"""


user, passwd = "aaa", "123"


def auth(auth_type):
    print("auth func:", auth_type)

    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == "local":
                username = input("username: ").strip()
                password = input("password: ").strip()

                if user == username and passwd == password:
                    print("\033[32;ImUser has passed authentication\033]Om")
                    res = func(*args, **kwargs)  # from home
                    print("_______after________")
                    return res
                else:
                    exit("\033[32;ImInvalid username or password\033]Om")
            elif auth_type == "ldap":
                print("其他操作。。。。。。。")
        return wrapper
    return outer_wrapper


def index():
    print("index page.......")


@auth(auth_type="local")
def home():
    print("home page.......")
    return "*****from home*******"


@auth(auth_type="ldap")
def bbs():
    print("bbs page........")


index()
print(home())
bbs()
