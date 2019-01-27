# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous, previous.next = self, head
        while previous.next and previous.next.next:
            first = previous.next
            second = first.next
            previous.next, second.next, first.next = second, first, second.next
            previous = first
        return self.next
