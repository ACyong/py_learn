class Fibs:
    def __init__(self,max):
         self.max = max

    def __iter__(self):
        self.cur_count = 0
        self.a = 1
        self.b = 1
        return self

    def __next__(self):
        if self.cur_count > self.max:
            raise StopIteration
        self.cur_count += 1
        if self.cur_count == 1:
            return 1
        if self.cur_count == 2:
            return 1
        self.a,self.b = self.b, self.a + self.b

        return self.b


L = [x for x in Fibs(6)]
print(L)
for x in Fibs(8):
    print(x)