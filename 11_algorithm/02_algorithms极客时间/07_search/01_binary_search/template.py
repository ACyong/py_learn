import time


# 二分法模板
def binarySearch(nums, target):
    left, right = 0, len(array) - 1  # NOQA
    while left <= right:
        mid = (left + right) // 2
        # mid = left + ((right - left) >> 1)
        # mid = left + ((right - left) // 2)
        if array[mid] == target:  # NOQA
            ...
        elif array[mid] < target:  # NOQA
            left = mid + 1
        elif array[mid] > target:  # NOQA
            right = mid - 1


def run_time(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        run = func(*args, **kwargs)
        end = time.time()
        print("Time cost: ", end - begin)
        return run

    return wrapper


@run_time
def binary_search(data_list, value):
    low = 0
    high = len(data_list) - 1
    while low <= high:
        middle = (low + high) // 2
        if data_list[middle] == value:
            return middle
        elif data_list[middle] < value:
            low = middle + 1
        else:
            high = middle - 1
    return


@run_time
def linear_search(data_list, value):
    for i in data_list:
        if data_list[i] == value:
            return i
    return


if __name__ == "__main__":
    L = list(range(1000000))
    binary_search(L, 4)
    linear_search(L, 4)
