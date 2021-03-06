# Python 面向对象


## 1.继承 inheritance 和 派生 derived
    继承的目的是延续旧的类的功能
    派生的目的是在旧的类的基础上添加新的功能

    作用：用继承和派生机制，可以将一些共有功能加在基类中，实现代码的共享，在不改变超类的代码的基础上改变原有的功能

    继承和派生名次：
        基类（base class）/ 超类（super class）/ 父类（father class）
        派生类（derived class）/ 子类（child class）


## 2.单继承：
    class 类名(超类名)：  # <<<--- 继承列表内可以添加超类
        .......

    思考：list类里只有append向末尾添加一个元素的方法，但没有向列表头添加元素的方法，
    试想能否为类表在不改变原有功能的基础上，添加一个insert_head(n)方法，在列表的头部（前部）添加元素
    class MyList(list):
        def insert_head(self, n):
            ......

    继承说明：任何类都直接或间接的继承自object类，object类是一切python3新式类的超类

    类中的base属性：
    __base__ 用来记录此类的基类

    覆盖 override
    覆盖是指在有继承关系的类中，子类中实现了与基类（超类）同名的方法，在子类实例调用该方法时，
    实际调用的是子类中的覆盖版本，这种现象叫覆盖

    super函数：
    super(type, obj): # 返回绑定超类的实例（要求obj必须为type类型的实例）
    super() 返回绑定超类的实例，等同于super(__class__, 实例方法的第一个参数)
    作用：用super可以调用父类的方法（可以是被覆盖版本的方法）

    显示调用基类的构造方法：
    当子类中实现在__init__方法时，基类的构造方法并不会调用（因为被覆盖了）

    用于类的函数：
    issubclass(cls, class_or_tuple)
    判断一个类是否继承其他的类，如果此类cls是class或tuple中的一个派生子类则返回True，否则返回False
    实例：
    class A:
        pass
    class B(A):
        pass
    class C(B):
        pass
    print(issubclass(B, A)) # True
    print(issubclass(B, (int, str))) # False

封装：enclosure
    1、封装的目的是让使用者通过尽可能的省的变量名（或）属性使用对象，
    2、封装是指隐藏类的实现细节，让使用者不关心这些细节。
    3、python不能实现C++等语言完全意义上的封装（是模拟的封装）

    私有实例变量和方法：
    python 中以双下划线__开头，不以双下划线结尾的标识符为私有变量/方法
    以__开头的实例变量为私有变量，子类和类外部无法直接使用
    以__开头的方法也为私有方法，子类和类外部无法直接使用

    实例：
    class A:
        def __init__(self, v):
            self.money = v # __money 为私有实例变量


多态
    是指多种状态，在有继承/派生关系的类中，调用基类对象的方法，实际能调用子类的覆盖方法的现象，叫多态
    多态说明：多态调用的方法写对象相关，不与类相关
    python的全部对象只有“运行时状态（动态）”，没有C++/Java里的编译时状态（静态）


- 装饰器类

> 在于比嵌套函数的方式更加整洁，而且包裹一个函数还是使用跟以前一样的语法

from functools import wraps
 
class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile
 
    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function
 
    def notify(self):
        # logit只打日志，不做别的
        pass

@logit()
def myfunc1():
    pass
    
来添加 email 的功能

class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)
 
    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass
        
从现在起，@email_logit 将会和 @logit 产生同样的效果，但是在打日志的基础上，还会多发送一封邮件给管理员。

面向对象语言：
    继承
    封装
    多态
    有：C++、Java、Python、C#

    多继承：multiple inheritance
    是指一个子类继承自两个或两个以上的基类

    语法：
        class 类名(超类名1,超类名2[,......]):

    多继承的问题（缺陷）
    标识符（名字空间）冲突问题，要谨慎使用多继承


PEP8 编码规范
    1、代码编排：
        1、使用4空格缩进，不使用TAB，更不允许用TAB和空格混合缩进
        2、每行最大长度79字节，超过部分使用反斜杠换行
        3、类和全局函数定义间隔两行，类内方法定义间隔一个空行，其他地方可以不加空行

    2、文档编排：
        1、其中import部分，按标准、三方和自己编码顺序依次排序，之间空一行
        2、不要在一句import语句中导入多个模块，不推荐：import os, sys
        3、尽可能用import xx， 而不是采用from XX import yy ， 因为可能出现名字冲突

    3、空格的使用：
        1、各种右括号前不加空格
        2、逗号，冒号，分号前不加空格
        3、函数的左括号前不要加空格，如func(1)
        4、序列的左括号前不要加空格，如L[2]
        5、操作符的左右各加一个空格，不要为了对齐佳空格
        6、函数默认参数使用的赋值符左右省略空格
        7、不要讲多条语句写在同一行，尽管使用；是允许的
        8、if/for/while语句中，即使执行语句只有一行，也必须另起一行（原则，避免不必要的空格）

