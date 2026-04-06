# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p = self.findNthFromEnd(dummy, n + 1)
        p.next = p.next.next
        return dummy.next

    def findNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2 = head, head
        for _ in range(n):
            p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2


