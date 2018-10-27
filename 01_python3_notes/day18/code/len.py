class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%r)" % self.data

    def __len__(self):
        print("__len__被调用")
        return len(self.data)



L2 = MyList("")
print("L2 = ", L2)
print("len(L2) = ", len(L2))
print("bool(L2) = ", bool(L2))