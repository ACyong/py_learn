# Definition for singly-linked list.
import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def __lt__(self, other):
            return self.val < other.val

        ListNode.__lt__ = __lt__

        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, l)
        dummy = ListNode()
        p = dummy
        while heap:
            node = heapq.heappop(heap)
            temp = node.next
            node.next = None
            p.next = node
            p = p.next

            if temp:
                heapq.heappush(heap, temp)
        return dummy.next
