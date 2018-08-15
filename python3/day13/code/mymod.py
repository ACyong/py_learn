# 实现一个自定义的模块提供其他模块使用
# 注意：模块的文件名必须是标识符

def mysum(n):
    s = 0
    for x in range(1, n+1):
            s += x
    return s

def myfun():
    print("myfun被调用")

name = "张飞"
name2 = "关羽"

print("mymode模块被加载…………")