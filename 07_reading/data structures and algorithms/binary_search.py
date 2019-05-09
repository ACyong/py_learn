import time


def run_time(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        run = func(*args, **kwargs)
        end = time.time()
        print("Time cost: ", begin - end)
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
    binary_search(list(range(1000000)), 4)
    linear_search(list(range(1000000)), 4)
