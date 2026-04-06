class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def create_link_list(n):
    head = Node(1)
    pre = head
    for i in range(2, n + 1):
        newNode = Node(i)
        pre.next = newNode
        pre = newNode
    pre.next = head
    return head


if __name__ == '__main__':
    n = 5  # 总的个数
    m = 2  # 数的数目
    if m == 1:  # 如果是1的话，特殊处理，直接输出
        print(n)
    else:
        head = create_link_list(n)
        pre = None
        cur = head
        while cur.next != cur:  # 终止条件是节点的下一个节点指向本身
            for i in range(m - 1):
                pre = cur
                cur = cur.next
            pre.next = cur.next
            cur.next = None
            cur = pre.next
        print(cur.value)
