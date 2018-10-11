class MyList:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "MyList(%r)" % self.value

    def __add__(self, other):
        return MyList(self.value + other.value)

    def __iadd__(self, rhs):
        self.value.extend(rhs.value)
        return self

    def __eq__(self, rhs):
        # return self.data == rhs.data

        if len(self.value) != len(rhs.value):
            return False
        for i in range(len(self.value)):
            if self.value[i] != rhs.value[i]:
                return False
        return True


L1 = MyList([1,2,3])
L2 = MyList([1,2,3])
if L1 == L2:
    print("相等")
else:
    print("不相等")

L2 += L1
print(L2)
