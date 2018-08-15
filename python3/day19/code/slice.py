class MyList:
    def __init__(self, lst):
        self.data = lst

    def __repr__(self):
        return "MyList(%r)" % self.data

    def __getitem__(self, i):
        print("__getitem__被调用, i的值是：", i)
        if isinstance(i, slice):
            print("这是切片")
            print("起始值是：", i.start)
            print("终止值是：", i.stop)
            print("步长是：", i.step)
        elif isinstance(i, int):
            print("这是索引取值")
        return self.data[i]

    def __setitem__(self, i, value):
        print("__setitem__被调用， i的值位：", i)
        self.data[i] = value


L1 = MyList([1, -2, 3, -4, 5])
L2 = L1[::2] # 切片取值 __getitem__方法
print("L2 = ", L2)
L3 = L1[3]
# value = L1["hello"]
