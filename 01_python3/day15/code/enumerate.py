numbers = [10086, 10000, 10010, 95588]
names = ['中国移动', '中国电信', '中国联通']
# L = [(0, '中国移动'), (1, '中国电信'), (2, '中国联通')]
for x in enumerate(names):
    print(x)
# 扩展
for no, n in enumerate(names):  # (等同于序列赋值)
    print(no, " ----->", n)
