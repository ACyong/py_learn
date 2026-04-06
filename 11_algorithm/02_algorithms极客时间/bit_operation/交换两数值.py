# 异或操作(无进位加法), 交换两数值
a, b = 1, 2
print(a, b)
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)
