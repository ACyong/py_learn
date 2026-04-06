# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p = self.findNthFromEnd(dummy, n+1)
        p.next = p.next.next
        return dummy.next

    def findNthFromEnd(self, head, k):
        p1, p2 = head, head
        for _ in range(k):
            p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2
