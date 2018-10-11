class MyList(list):
    def insert_head(self, n):
        # self[0:0] = n
        self.insert(0, n)

l = MyList([1, 2])
l.insert_head(1)
print(l)