# 时间复杂度O(n^2)
def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot+1):
            if a_list[location] > a_list[position_of_max]:
                position_of_max = location
        a_list[fill_slot], a_list[position_of_max] = a_list[position_of_max], a_list[fill_slot]


unordered_list = [1, 23, 12, 45, 32, 645, 7, 123, 35, 77]
selection_sort(unordered_list)
print(unordered_list)
