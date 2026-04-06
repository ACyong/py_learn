# 基础写法
def quick_sort(a_list):
    length = len(a_list)
    if length <= 1:
        return a_list
    pivot = a_list[0]  # 基准值
    left = [i for i in a_list[1:] if i < pivot]
    right = [i for i in a_list[1:] if i >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


"""
快速排序的时间复杂度有可能达到 O(n2) 这个量级，也就是退化成和选择排序、插入排序等算法一样的时间复杂度。
只有当基准值每次都能将排序区间中的数据平分时，时间复杂度才是最好情况下的 O(nlogn)
"""


def quick_sort2(a_list):
    # 三点取中法能帮助我们选出更加合理的基准值，保证快速排序的运行效率；
    def select_pivot(a_list, left, right):
        mid = (left + right) // 2
        compare_list = (a_list[left], a_list[right], a_list[mid])
        max_num = max(compare_list)
        min_num = min(compare_list)
        return sum(compare_list) - max_num - min_num

    # 分区操作优化 partition 的操作，通过减少程序实现中的比较操作，来提高程序的运行效率。
    def partition(a_list, left, right):
        pivot = select_pivot(a_list, left, right)  # 基准值
        while left < right:
            while left < right and a_list[right] >= pivot:
                right -= 1
            a_list[left] = a_list[right]  # 比基准小的交换到前面
            while left < right and a_list[left] <= pivot:
                left += 1
            a_list[right] = a_list[left]  # 比基准大交换到后面
        a_list[left] = pivot  # 基准值的正确位置，也可以为 nums[right] = pivot
        return left  # 返回基准值的索引，也可以为 return right

    # 单边递归法可以使快排过程中的递归调用次数减少一半，并且，这种优化方法也可以使用在所有和快速排序类似的程序结构中；
    def quick_sort_helper(a_list, left, right):
        while left < right:
            pivot_index = partition(a_list, left, right)
            quick_sort_helper(a_list, pivot_index + 1, right)  # 右序列
            right = pivot_index

    quick_sort_helper(a_list, left=0, right=len(a_list) - 1)


if __name__ == '__main__':
    unordered_list = [23, 3, 12, 45, 32, 645, 7, 123, 35, 77]
    print(quick_sort(unordered_list))

    unordered_list = [23, 3, 12, 45, 32, 645, 7, 123, 35, 77]
    quick_sort2(unordered_list)
    print(unordered_list)

    # 一组无序的数字，找到其中排名第 k 位的数字
    unordered_list = [12, 34, 123, 452, 223, 11, 3, 6, 2346, 3]
    quick_sort2(unordered_list)
    print(unordered_list, unordered_list[4])
