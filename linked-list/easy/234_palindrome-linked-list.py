#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.cn/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (57.22%)
# Likes:    2103
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,2,1]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
# 
# 
# 
# Follow up: Could you do it in O(n) time and O(1) space?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head_list = []
        cur = head
        while cur:
            head_list.append(cur.val)
            cur = cur.next
        return head_list == head_list[::-1]
# @lc code=end

