# 基本的二分搜索: 找到对应值
def binary_search(nums, target):
    if not nums:
        return -1

    # 初始化 right 的赋值是 len(nums) - 1, 因为索引⼤⼩为 len(nums) 是越界的
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # 不要出现 else，⽽是把所有情况⽤ else if 写清 楚，这样可以清楚地展现所有细节
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1


# 寻找左侧边界的⼆分搜索:  nums 中⼩于 target 的元素有几个
def binary_search1(nums, target):
    if not nums:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 类似之前算法的处理⽅式
    # if left == len(nums):
    #     return -1
    # return left if nums[left] == target else -1
    return left


# 寻找左侧边界的⼆分搜索:  nums 中大于 target 的元素有几个
def binary_search2(nums, target):
    if not nums:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 类似之前算法的处理⽅式
    # if left == 0:
    #     return -1
    # return left - 1 if nums[left - 1] == target else -1
    return left - 1


if __name__ == '__main__':
    print(binary_search([1, 2, 2, 2, 4], 2))
    print(binary_search1([1, 2, 2, 2, 4], 2))
    print(binary_search2([1, 2, 2, 2, 4], 2))
