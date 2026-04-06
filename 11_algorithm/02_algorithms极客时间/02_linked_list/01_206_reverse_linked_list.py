# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def reverseList1(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        last = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return last
