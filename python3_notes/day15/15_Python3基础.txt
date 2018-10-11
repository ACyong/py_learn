1、迭代器 Iterator
    迭代器是指用 iter(obj) 函数返回的对象（实例） 间接访问可迭代对象的一种方式
    迭代器可以用 next(it) 函数依次获取可迭代对象的值

    实例：
        L = [1,3,5,7,9] # L为可迭代对象
        it = iter(L) # it 绑定迭代器
        v = next(it) # v 绑定
        print(v) # 1
        print(next(it)) # 3
        print(next(it)) # 5
        print(next(it)) # 7
        print(next(it)) # next 函数内触发StopIteration异常通知
        说明：
           迭代器是访问可迭代对象的一种方式（另一种方式for 语句）
           迭代器只能往前取值，不会后退
           用iter()函数可以返回一个可迭代对象的迭代器

    迭代器函数
        iter(iterable) 从可迭代对象中返回一个迭代器，iterable必须是一个可迭代对象
        next(iterable) 从迭代器iterable 中获取下一个记录，如果无法获取下一条记录，则触发StopIteration，异常来通知调用者已无数据可提供
        实例：
            以前学过的可迭代对象：str、list、tuple、dict、set、frozenset，range()函数返回值，map()函数的返回值，
                               filter()函数的返回值，sorted()函数返回的是列表，zip，enumerate


2、生成器：Generator（python2.5 之后）
    生成器是指能够动态提供数据的对象，只用在调用的时候才会生成相应的数据，只记录当前数据，生成器对象也是迭代器对象，当迭代超出范围后，产生一个StopIteration
    生成器有两种：（只能用for 语句、next 函数、生成器属性取值，取值时生成器才会生成要用到的数据）
        1、生成器函数
        2、生成器表达式

    生成器函数：
        含有yield 语句的函数是生成器函数，此函数调用将返回一个生成器对象 yield 翻译为生成、产生
        yield语句：
            语法：yield 表达式
            说明：yield 用于def 函数中，目的是将此函数作为生成器函数使用
                 yield 用来生成数据，此数据提供给迭代器的next(it) 函数使用
                 yield 记住当前执行环境暂停函数，并返回数据给调用处，再次取数据时执行回到yield 语句处向下执行

    练习：写一个生成器函数，用于生成n 个斐波那契额数，n 以参数的形式传入

    答案：
        def fib(max):
            n, a, b = 0, 0, 1
            while n < max:
                # print(b)
                yield b
                a, b = b, a + b
                n = n + 1
            # return "done"

        g = fib(6)
        while True:
            try:
                x = next(g)
                print("g", x)
            except Exception as e:
                print("Generator return value:", e.value)
                break

    生成器函数说明：
        生成器函数的调用将返回一个可迭代对象
        生成器函数调用return 语句，当迭代超出范围后，产生一个StopIteration 异常后加return 的值（如：StopIteration: done）
        生成器函数每次用next() 函数取值时才会执行，遇到yield语句后将停止执行，并返回数据

    生成器表达式：generator expression
        语法：(表达式 for 变量 in 可迭代对象 [if 真值表达式])
             注：[]内的if部分可以省略，形式很像列表生成式，只是把中括号改成了小括号
        作用：用推导式的形式生成一个新的生成器，可以用生成器的属性 .__next__() 取值

        实例：
            In [10]: a = (x*2 for x in range(5))  # 使用生成器表达式来创建一个生成器

            In [11]: a
            Out[11]: <generator object <genexpr> at 0x103b887d8>

            In [12]: s = iter(a)  # 使用iter 函数返回一个迭代器

            In [13]: s
            Out[13]: <generator object <genexpr> at 0x103b887d8>

            In [14]: a.__next__()  # 生成器使用 .__next__ 属性取值
            Out[14]: 0

            In [15]: next(s)  # 迭代器使用next 函数取值
            Out[15]: 2

            In [16]: next(a)  # 因为生成器也是可迭代对象，所以也可以用next 函数取值
            Out[16]: 4

            In [17]: a.__next__()  # 如果无法获取下一条记录，则触发StopIteration
            Traceback (most recent call last):
            StopIteration

    生成器表达式和列表推导式的区别：
        1、生成器表达式中产生的数据是现用现生成，不记住之前生成的数据，也不能使用已经生成过的数据，当迭代超出范围后，产生一个StopIteration
        2、列表推导式会一次性生成很多个数据

    生成器的并发：
        import time

        def consumer(name):
            print("%s 准备吃包子！" % name)
            while True:
                baozi = yield
                print("包子[%s] 来了，被[%s] 吃了！" % (baozi, name))

        def producer(name):
            c = consumer("A")
            c2 = consumer("B")
            y = c.__next__()
            y1 = c2.__next__()
            print("准备做包子！", y, y1)
            for i in range(10):
                time.sleep(1)
                print("做了2 个包子")
                c.send(i)
                c2.send(i)

        producer("庄")


3、迭代工具函数
    迭代工具函数的作用是生成一个个性化的可迭代对象
    zip(iter[, iter,....]) 返回一个zip对象，此对象用于生成元组，此元组的个数由最小的可迭代对象决定
    实例：
        numbers = [10086, 10000, 10010, 95588]
        names = ['中国移动', '中国电信', '中国联通']
        for x in zip(numbers, names):
            print(x)
    结果：
        (10086, '中国移动')
        (10000, '中国电信')
        (10010, '中国联通')

    enumerate(iterator[, start])
    生成带索引的枚举对象，返回迭代类型为索引-值对（index, value）的元组，默认索引从零开始，也可以指定start
    实例：
        numbers = [10086, 10000, 10010, 95588]
        names = ['中国移动', '中国电信', '中国联通']
        # L = [(0, '中国移动'), (1, '中国电信'), (2, '中国联通')]
        for x in enumerate(names):
            print(x)
        # 扩展
        for no, n in enumerate(names):  # (等同于序列赋值)
            print(no, " ----->", n)
    结果：
        (0, '中国移动')
        (1, '中国电信')
        (2, '中国联通')
        0  -----> 中国移动
        1  -----> 中国电信
        2  -----> 中国联通


练习：写一个程序，输入任意行文字，当输入空行时结束输入打印带有行号的输出结果
     如：$ python3 mytest.py
        请输入：hello
        请输入：world
        请输入：bye
        请输入：<回车>
        输出如下：
        第一行：hello
        第二行：world
        第三行：bye


文件操作
    文件是指用于数据存储的基本单位，通常用于长期存储数据（任何计算机系统同时打开的文件是有最大数限制的）
    文件操作的步骤：
        1、打开文件
        2、读/写文件
        3、关闭文件

    文件的打开函数：
        open(文件名, mode = 'rt', [encoding='字符集']) 打开一个文件，返回文件流对象，是按行可迭代的(迭代器)，如果打开失败则会触发IOError错误

    mode 模式字符的含义：
        'r' 以只读方式打开（默认）
        'w' 以只写方式打开, 删除原有文件内容（如果文件不存在则创建此文件并以只写方式打开）
        'x' 创建一个新文件，并以写模式打开，如果文件已存在，则产生FileExistError错误
        'a' 以只写方式打开，如果原文件有内容，则追加到文件末尾
        'b' 以二进制模式打开
        't' 以文本模式打开（默认）
        '+' 为更新内容打开一个磁盘文件（可读可写）
        'r+' 可读可写可追加
        'w+' 可写可读
        'U' 表示在读取时，可以将 \r \n \r\n 自动转换为\n，配合r r+ 使用

    文件常用的方法：
        F.read([size=-1])  从一个文件流中最多读取size个字符（或字节）中文与英文都占一个字符，默认读取全部
        F.readline()  读取一行数据，如果到达文件尾则返回空行
        F.readlines([max_chars = -1])  返回每行字符串的列表，max_chars为最大字符（或字节）数
        F.write(data)  写一个字符串（或字节串），返回写入的个数
        F.writelines(lines)  将字符串的列表写入文件
        F.flush()  把文件写入文件对象的缓存内容写入磁盘
        F.tell()  返回当前文件流的绝对位置(文件的读写位置是以字节为单位的，一般不对文本文件进行操作)
        F.seek(offset, whence = 0)  改变数据流的位置，返回新的绝对位置
               offset 偏移量 （大于0的数，代表向文件末尾方向移动，小于0的数 ，代表向文件头方向移动）
               whence 相对位置 （0 代表从文件头开始偏移 1 代表从当前位置开始偏移 2 代表从文件尾开始偏移）

    对文件的增删改查：
        直接使用文件对象的方法只能做到对文本文件的追加和清空，使用一下方法可以实现对指定内容的增删改查：
            import sys

            find_str = sys.argv[1]
            replase_str = sys.argv[2]

            f = open("data2.txt", 'r')
            f_new = open("data3.txt", "w")

            for line in f:
                if find_str in line:
                    line = line.replace(find_str, replase_str)
                f_new.write(line)

            f.close()
            f_new.close()

    文件的关闭方法：
        F.close()  # F代表open返回的文件流对象
        F.closed()  # 返回文件是否关闭

    with 语句：
        为了避免打开文件后忘记关闭，可以通过管理上下文，即：
            with open("text.txt", "r") as f:
                pass
        如此方式，当用with 代码块执行完毕时，内部会自动关闭并释放文件资源

        在python2.7 后，with 支持同时对多个文件的上下文进行管理，即：
            with open("text1.txt", "r") as f1, open("test2.txt", "r") as f2:
                pass


练习：先用文本编辑器写一个文件“mynotes.txt” 写入一些数据，写一个程序read_notes.py,读取每一行数据，
     加上行号后显示在屏幕终端上

练习：写一个程序，从键盘读入一些字符串，当输入空行时结束
     将以上读入内容写入文件“input.txt”中（）要求：键盘操作和文件内容一致

练习：
    1、用生成器函数，生成素数，给出起始值为begin和终止值end，此生成器函数为：
       def myprimes(begin, end):
       用于生成begin～end 之间的素数（不包含end）
       L = [x for x in myprimes(10, 20)]
       print(L) # [11, 13, 17, 19]
    2、写一个生成器函数，参数为n，生成斐波那契数列的前n个数
       def fibonacci(n):
          .......
       L = [x for x in fibonacci(7)] # L = [1, 1, 2, 3, 5, 8, 13]
    3、修改之前的学生管理系统，添加保存数据功能菜单中添加功能如下：
       | 9）保存数据到文件（si.txt）|
       | 10）从文件中读取数据（si.txt）|

       文件格式为：
          姓名，年龄， 成绩<回车换行>
练习：
    1、现有一个列表alist = ['hello', 'world'], 写一个程序要求实现如下输出：
       index 0 : hello
       index 1 : world

    2、写一个程序，要求实现如下功能：
       1）创建一个文件student_info.txt
       2) 文件中写入如下两行内容：
          name:Bob age:30 score:90
          name:Lucy age:25 score:99

    3、写一个生成器函数myyield(),将练习2中student_info.txt中的两行内容生成一个成器
       然后用for语句打印这两行内容
       for x in myyield():
           print(x)

