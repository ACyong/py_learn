1、比较运算符：实数可以比较大小，复数不能比较大小
    <  小于
    <= 小于等于
    >  大于
    >= 大于等于
    == 等于
    != 不等于（<>仅用于python2中）

    语法：左表达式 < 右表达式
    说明：比较运算符返回布尔类型的值 True/False
    实例：
        1 < 2       # True
        1 < 2 < 3   # True
        x = 1000
        1 <= x <= 100   # 判断x是否在[1，100]这个区间


2、函数调用（函数调用是“表达式”）
    语法：函数名(传参列表)
    语法说明：函数调用是表达式，通常用于返回一个对象

    练习：（用交互模式来做）
        将数字3.14用变量pi绑定
        将pi变量转为整数用i变量绑定
        将pi变量与i变量相减，结果存于f变量中
        判断f是否等于0.14
        删除所有变量

        答案：
            >>> pi = 3.14
            >>> i = int(pi)
            >>> f = pi - i
            >>> f == 0.14
            False
            >>> f
            0.14000000000000012
            >>> del pi
            >>> del i
            >>> del f


3、预置（内建）的数值函数
    abs(x)                    # 取x的绝对值
    round(number[，ndigits])  # 对小数数值进行四舍五入，ndigits是小数向右取整的位数，负数向左取整
    pow(x，y，z=None)         # 相当于 x ** y 或 x ** y % z
    hash(x) 用于获取取一个对象（字符串或者数值等）的哈希值
    help()          # 查看函数帮助：
      >>> help(abs)   # 查看abs函数帮助


4、基本输入输出函数
    基本输入   input 函数：（python2 中使用raw_input）
    作用：从标准输入设备上读取一个字符串（末尾的换行字符会被删除）
    格式：input("提示字符串")
    注：返回输入的字符串

    基本输出函数 print函数
    作用：将一系列的值以字符串的形式输出到标准输设备上（默认为终端）默认打印换行
    格式：print(value,....,sep=' ', end='\n', flush=Flase, file=sys.stdout)
    关键字参数详解：
        sep 两个值之间的分隔符，默认为一个空格
        end 输出完毕后在字符串流末尾自动追加一个字符串，默认为换行符号‘/n’
        flush  是否立即输出
        file   文件流对象，默认为sys.stdout

    实例：模拟打印进度条

        答案：
            import sys
            import time

            for i in range(20):
                sys.stdout.write("#")
                sys.stdout.flush()
                time.sleep(0.1)
            else:
                print()


5、语句：statment
    赋值语句
    del语句
    什么是语句：语句是由一些表达式组成的，通常一条语句可以独立完成一部分事情并形成结果
    注：一条语句建议写在一行内，多条语句写在一行内可以用分号 ; 分开
    实例：
        print（“hello”）
        x = 100 + 200
        x = 1+2+3+4+5+6+8\  显式换行：折行符号 \（反斜线）
            +85+9+10        折行符号必须放在一行的末尾，
        print("he\          目地是告诉解释器下一行也是本行的语句
            llo")           隐式换行：所有的括号的内容换行，称为隐式换行 () [] {}


6、if 语句
    作用：让程序根据条件有选择性的执行某条语句或某些语句

    语法：
        if 真值表达式1：
            语句1。。。。
        elif 真值表达式2：
            语句2。。。。
        elif 真值表达式3：
            语句3。。。。
        else：
            语句4

    语法说明：
        1、elif子句可有0个，1个或多个
        2、else 子句可有1个，也可以没有，且只能放在最后
        3、所有的真值表达式自上而下进行判断，只要有一个为真值，则执行内部语句，然后结束当前的if语句的执行

    if 语句的嵌套：
       if 语句本身是由多条语句组成的一条复合语句
       if 语句可以作为语句且套到另一个语句内部


7、三元运算符：
    语法：
        表达式1 if 真值表达式 else 表达式2
    作用：
        根据真值表达式返回的结果不确定是执行表达式1还是表达式2，并返回结果

    实例：# 商场促销，满100减20
        s = input("请输入商品的总金额：")
        money = int(s)
        pay = money - 20 if money >= 100 else money

    练习：
        输入一个数，打印这个数的绝对值（要求用条件表达式，不允许用abs函数）
        a = int(input("输入一个数："))
        b = a if a >= 0 else -a
        print("这个数的绝对值为：", b)


8、pass 语句：
    作用：通常用来填充语法空白
         pass 又名空语句

    语法：
        pass

    实例：
        # 判断一个学生的成绩，如果不再0-100之间，提示不合法的输入
        s = input("请输入学生成绩：")
        score = int(s)
        if 0 <= score <= 100:
            # 啥也不做
            pass
        else：
            print("不合法的输入！")


9、布尔运算：
    运算符：
        not   and   or
    布尔"非"操作 not（取反）
    语法：not X   # x表示一个值
    作用：对x进行布尔取非操作，如bool(x)为True，则返回False，否则返回True
    实例： not True   # 返回False
          not False  # 返回True

    布尔"与"操作 and
    语法：x and y
         注：x，y代表表达式
    作用：优先返回假值对象（谁为假就选谁），当x的布尔值为假False时，返回x，否则返回y

    布尔"或"操作 or
    语法：x or y
    作用：优先返回真值对象，当x为True时，返回x，否则返回y
    实例：>>> True or True
         True
         >>> False or True
         True
         >>> True or False
         True
         >>> False or False
         False


练习：
    1、如何把字符串“6.6”转换为浮点型，请写出语句
      float('6.6')

    2、给了一个年份，判断是否为闰年并打印每四年一闰，每百年不闰，四百年又闰
      year = int(input("请输入年份："))

      if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
          print("闰年")
      else:
          print("非闰年")

    3、输出字符串：Tom's pet is a cat.The cat's name is "Tiechui"  # 用转义符号实现
      print("Tom's pet is a cat.The cat's name is\"Tiechui\"")

