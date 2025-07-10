# @before-stub-for-debug-begin
from python3problem86 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        small_dummy = ListNode(0)
        large_dummy = ListNode(0)
        small = small_dummy
        large = large_dummy
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        small.next = large_dummy.next
        large.next = None
        return small_dummy.next

# @lc code=end

