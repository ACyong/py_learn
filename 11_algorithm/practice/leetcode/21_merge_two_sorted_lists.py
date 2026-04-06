# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy
        p1, p2 = list1, list2

        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p.next, p1 = p1, p1.next
            else:
                p.next, p2 = p2, p2.next
            p = p.next

        if p1 is not None:
            p.next = p1
        if p2 is not None:
            p.next = p2

        return dummy.next
