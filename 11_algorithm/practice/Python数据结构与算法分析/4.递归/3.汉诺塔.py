"""
递归算法要遵守三个重要的原则:
(1) 递归算法必须有基本情况 ;
(2) 递归算法必须改变其状态并向基本情况靠近;
(3) 递归算法必须递归地调用自己。

题目: 修行者有 3 根柱子和 64 个依次叠好的金盘 子，下面的盘子大，上面的盘子小。
修行者的任务是将 64 个叠好 的盘子从一根柱子移动到另一根柱子，
同时有两个重要的限制条件: 每次只能移动一个盘子，并且大盘子不能放在小盘子之上
"""


def move_tower(height, from_pole, to_pole, with_pole):
    """汉诺塔问题"""
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(fp, tp):
    print("moving disk from %d to %d" % (fp, tp))


move_tower(3, 1, 3, 2)
