# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1, p2 = head, head
        for _ in range(k):
            p1 = p1.next
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        return p2
