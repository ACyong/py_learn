class MyList:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "MyList(%r)" % self.value

    def __add__(self, other):
        return MyList(self.value + other.value)


L1 = MyList([1,2,3])
L2 = MyList([4,5,6])
L3 = L1 + L2
print(L3)
L3 = L2 + L1
print(L3)