"""
递归算法要遵守三个重要的原则:
(1) 递归算法必须有基本情况 ;
(2) 递归算法必须改变其状态并向基本情况靠近;
(3) 递归算法必须递归地调用自己。
"""


def rec_dc(coin_value_list, change, known_results):
    """递归找零钱"""
    min_coins = change
    if change in coin_value_list:
        known_results[change-1] = 1
        return 1
    elif known_results[change-1] > 0:
        return known_results[change-1]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + rec_dc(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change-1] = min_coins
    return min_coins


print(rec_dc([1, 5, 10, 25], 63, [0] * 63))
