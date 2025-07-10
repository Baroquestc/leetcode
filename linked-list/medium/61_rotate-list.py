#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.cn/problems/rotate-list/description/
#
# algorithms
# Medium (41.42%)
# Likes:    1130
# Dislikes: 0
# Total Accepted:    445.6K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, rotate the list to the right by k places.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        # 1. get the length of the list
        # 2. connect the tail to the head
        # 3. find the new tail
        # 4. disconnect the new tail from the new head
        # 5. return the new head
        # TC: O(n)
        # SC: O(1)
        # 1. get the length of the list
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        # 2. connect the tail to the head
        tail.next = head
        # 3. find the new tail
        k = k % length
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        # 4. disconnect the new tail from the new head
        new_head = new_tail.next
        new_tail.next = None
        # 5. return the new head
        return new_head

# @lc code=end

