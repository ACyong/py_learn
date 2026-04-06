from typing import List


class Solution26:
    # 快慢指针
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution83:
    # 快慢指针
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        slow, fast = head, head
        while fast:
            if slow.val != fast.val:
                slow.next = fast
                slow = fast
            fast = fast.next
        slow.next = None
        return head


class Solution27:
    # 快慢指针
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


class Solution283:
    # 快慢指针
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
