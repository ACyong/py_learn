"""
递归算法要遵守三个重要的原则:
(1) 递归算法必须有基本情况 ;
(2) 递归算法必须改变其状态并向基本情况靠近;
(3) 递归算法必须递归地调用自己。

题目: 将整数转换成以 2~16 为进制基数的字符串
"""


def to_str(num, base):
    """将整数转换成任意进制的字符串"""
    convert_string = "0123456789ABCDEF"
    if num < base:
        return convert_string[num]
    else:
        return to_str(num // base, base) + convert_string[num % base]


print(to_str(10, 2))
