"""
解决组团 or 配对问题

基本操作:
1. makeSet(s): 建立一个新的并查集, 其中包含s个单元素集合
2. unionSet(x, y): 把元素x 和 元素y 所在的集合合并, 要求x和y所在的集合不相交, 如果相交则不合并
3. find(x): 找到元素x 所在的集合的代表, 该操作也可以用于判断两个元素是否位于同一个集合, 只要将它们各自的代表比较一下就可以了
"""


class DisjointSet(object):
    def __init__(self, p):
        self.p = [i for i in range(n)]  # NOQA

    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p1] = p2

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:  # 路径压缩
            x, i, p[x] = i, p[i], root
        return root
