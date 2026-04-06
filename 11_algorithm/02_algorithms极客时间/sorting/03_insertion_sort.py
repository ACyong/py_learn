# 时间复杂度O(n^2)
def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position-1
            a_list[position] = current_value


unordered_list = [23, 12, 45, 32, 645, 7, 123, 35, 77]
insertion_sort(unordered_list)
print(unordered_list)
