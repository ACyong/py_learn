# 时间复杂度大概介于O(n) 和O(n^2) 之间
def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2


def gap_insertion_sort(a_list, start, gap):
    for i in range(start+gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position-gap
        a_list[position] = current_value


unordered_list = [23, 12, 45, 32, 645, 7, 123, 35, 77]
shell_sort(unordered_list)
print(unordered_list)
