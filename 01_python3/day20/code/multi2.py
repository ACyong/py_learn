class A:
    def __init__(self):
        self.name = 'A'

class B:
    def __init__(self):
        self.name = 'B'

class AB(A, B):
    def info(self):
        print(self.name) # 请问打印结果是什么

ab = AB()
ab.info()
