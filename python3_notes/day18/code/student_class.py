class Student:
    """学生类"""

    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s

    def get_infos(self):
        s = '|%s|%s|%s|' % (self.name.center(6),
                            str(self.age).center(6), str(self.score).center(6))
        return s

    def get_file_info(self):
        s = self.name + ',' + \
            str(self.age) + ',' + \
            str(self.score)
        return s

    def get_score(self):
        return self.score



