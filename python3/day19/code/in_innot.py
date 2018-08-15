class MyList:
    def __init__(self, lst):
        self.data = lst

    def __repr__(self):
        return "MyList(%r)" % self.data

    def __contains__(self, value):
        # return self.data.count(value) > 0
        # return value in self.data
        # return self.data.__contains__(value)
        for x in self.data:
            if x == value:
                return True
        return False



L1 = MyList([1, -2, 3, -4, 5])
if 2 in L1:
    print("2 in L1 内")
else:
    print("2 不在 L1 内")

