"""
快速选择算法可以用来快速查找一个序列中排名第 k 位的元素
"""


def quick_select(a_list, k):
    if len(a_list) <= k:
        return a_list
    pivot = a_list[-1]
    right = [pivot] + [x for x in a_list[:-1] if x >= pivot]
    r_len = len(right)
    if r_len == k:
        return right
    if r_len > k:
        return quick_select(right, k)
    else:
        left = [x for x in a_list[:-1] if x < pivot]
        return quick_select(left, k - r_len) + right


if __name__ == '__main__':
    a_list = [12, 15, 22, 5, 63, 1, 53, 8, 34, 12, 75, 92, 1]
    print(quick_select(a_list, 3))
