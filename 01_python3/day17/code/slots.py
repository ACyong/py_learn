class Student:
    """__slots__列表限定此类所创建的对象只能有如下是那个实例变量，
    不能有其他的实例变量，否则会出错
    """
    __slots__ = ["name", "age", "score"]

    def __init__(self, n, a, s):
        self.name, self.age, self.score = n, a, s


s1 = Student("name1", 10, 100)
print("s1.score = ", s1.score)
# s1.csore = 60 # 故意写错
print("s1.score = ", s1.score)
