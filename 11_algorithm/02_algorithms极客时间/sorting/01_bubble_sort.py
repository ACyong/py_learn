# 时间复杂度O(n^2)
def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]

                # 异或操作(无进位加法), 交换两数值
                # a_list[i] = a_list[i] ^ a_list[i + 1]
                # a_list[i + 1] = a_list[i] ^ a_list[i + 1]
                # a_list[i] = a_list[i] ^ a_list[i + 1]


def short_bubble_sort(a_list):
    # 这种写法叫短冒泡, 优于上面的写法
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        pass_num -= 1


unordered_list = [23, 12, 45, 32, 645, 7, 123, 35, 77]
bubble_sort(unordered_list)
print(unordered_list)

unordered_list = [23, 12, 45, 32, 645, 7, 123, 35, 77]
short_bubble_sort(unordered_list)
print(unordered_list)
