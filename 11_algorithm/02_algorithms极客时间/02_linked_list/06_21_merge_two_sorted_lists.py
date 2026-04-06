# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    链表的算法题中是很常见的「虚拟头结点」技巧，也就是 dummy 节点。
    如果不使用 dummy 虚拟节点，代码会复杂很多，而有了 dummy 节点这个占位符，
    可以避免处理空指针的情况，降低代码的复杂性。

    什么时候需要用虚拟头结点？这里总结下：当你需要创造一条新链表的时候，可以使用虚拟头结点简化边界情况的处理。
    比如说，让你把两条有序链表合并成一条新的有序链表，是不是要创造一条新链表？
    再比你想把一条链表分解成两条链表，是不是也在创造新链表？这些情况都可以使用虚拟头结点简化边界情况的处理。
    """
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                p.next, list1 = list1, list1.next
            else:
                p.next, list2 = list2, list2.next
            p = p.next

        if list1 is None:
            p.next = list2
        if list2 is None:
            p.next = list1

        return dummy.next
