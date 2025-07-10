#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.cn/problems/reverse-linked-list/description/
#
# algorithms
# Easy (76.07%)
# Likes:    3903
# Dislikes: 0
# Total Accepted:    2.4M
# Total Submissions: 3.1M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: [2,1]
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# 
# 
# 
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from hmac import new


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1.迭代
        # if not head:
        #     return
        # pre, cur = None, head

        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = tmp

        # return pre

        # 2.递归
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head
# @lc code=end

