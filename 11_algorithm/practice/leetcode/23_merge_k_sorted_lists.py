# Definition for singly-linked list.
import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None
        for list_head in lists:
            res = self.mergeTwoLists(res, list_head)
        return res

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        p = dummy

        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1 is None:
            p.next = l2
        if l2 is None:
            p.next = l1

        return dummy.next

    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sort_list = []
        for l in lists:
            while l:
                heapq.heappush(sort_list, l.val)
                l = l.next

        dummy = ListNode()
        p = dummy
        while sort_list:
            p.next = ListNode(heapq.heappop(sort_list))
            p = p.next
        return dummy.next
