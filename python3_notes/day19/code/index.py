class MyList:
    def __init__(self, lst):
        self.data = lst

    def __repr__(self):
        return "MyList(%r)" % self.data

    def __getitem__(self, i):
        print("__getitem__被调用, i的值是：", i)
        return self.data[i]

    def __setitem__(self, i, value):
        print("__setitem__被调用， i的值位：", i)
        self.data[i] = value


L1 = MyList([1, -2, 3, -4, 5])
print(L1[3])

L1[1] = 2
print(L1)





