L = [1, 2, 3]
# def f(n = 0, lst = []):
#     lst.append(n)
#     print(lst)
def f(n = 0, lst = None):
    if lst is None:
        lst = [] # 创建一个新列表
    lst.append(n)
    print(lst)
f(4, L)
f(5, L)
print(L)
f(100)
f(200)
print(L)