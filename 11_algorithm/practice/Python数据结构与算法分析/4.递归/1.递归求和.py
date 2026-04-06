"""
递归算法要遵守三个重要的原则:
(1) 递归算法必须有基本情况 ;
(2) 递归算法必须改变其状态并向基本情况靠近;
(3) 递归算法必须递归地调用自己。

找整个递归的终止条件：递归应该在什么时候结束？
找返回值：应该给上一级返回什么信息？
本级递归应该做什么：在这一级递归中，应该完成什么任务？

题目: 计算数字列表[1, 3, 5, 7, 9] 的和
"""


def list_sum(num_list):
    """循环求和函数"""
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum


def recursion_sum(num_list):
    """递归求和"""
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + recursion_sum(num_list[1:])


print(list_sum([1, 3, 5, 7]), recursion_sum([1, 3, 5, 7]))
