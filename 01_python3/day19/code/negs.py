class MyList:
    def __init__(self, lst):
        self.data = lst

    def __repr__(self):
        return "MyList(%r)" % self.data

    def __neg__(self):
        return MyList([-x for x in self.data])
        # L = []
        # for x in self.data:
        #     L.append(-x)
        # return MyList(L)


L1 = MyList([1, -2, 3, -4, 5])
print("L1 = " , L1)

L2 = -L1
print("L2 = ", L2)


