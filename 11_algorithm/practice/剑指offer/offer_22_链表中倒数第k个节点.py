# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1 = head
        count = 0
        while p1:
            count += 1
            p1 = p1.next
        end = count - k
        p2 = head
        while end:
            end -= 1
            p2 = p2.next
        return p2

    def getKthFromEnd1(self, head: ListNode, k: int) -> ListNode:
        """让 p1 和 p2 同时向前走，p1 走到链表末尾的空指针时走了 n - k 步，
        p2 也走了 n - k 步，也就是链表的倒数第 k 个节点"""
        p1, p2 = head, head
        for _ in range(k):
            p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2
