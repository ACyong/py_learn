# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """每当慢指针 slow 前进一步，快指针 fast 就前进两步，
        这样，当 fast 走到链表末尾时，slow 就指向了链表中点。"""
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
