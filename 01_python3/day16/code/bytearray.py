
# 练习：有一个bytearray， ba = bytearray(b'a1b2c3d4')
#      1)、如何得到如下字符中‘1234’ 和‘abcd’
#      2)、将上述bytearray改为：bytearray（b'A1B2C3D4'）

ba = bytearray(b'a1b2c3d4')

bn = ba[::2]
# bd = ba[1::2]
ba.reverse()
bd = ba[::2]

print(bn, bd)


