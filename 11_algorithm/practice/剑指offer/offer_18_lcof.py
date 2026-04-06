# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next

        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur.val == val:
            pre.next = cur.next

        return head

    def deleteNode1(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        cur = head
        while cur.next and cur.next.val != val:
            cur = cur.next
        if cur.next is not None:
            cur.next = cur.next.next
        return head
