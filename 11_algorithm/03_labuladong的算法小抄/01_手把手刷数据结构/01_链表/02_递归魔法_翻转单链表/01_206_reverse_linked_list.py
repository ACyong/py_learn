# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverseList1(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur is None:
            node = cur.next
            cur.next = pre
            pre = cur
            cur = node
        return pre
