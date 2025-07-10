# @before-stub-for-debug-begin
from python3problem83 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (54.31%)
# Likes:    1182
# Dislikes: 0
# Total Accepted:    755.6K
# Total Submissions: 1.4M
# Testcase Example:  '[1,1,2]'
#
# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,1,2]
# 输出：[1,2]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next:
            return head
        pre, cur = head, head.next
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = pre.next
                cur = cur.next
        return pre
# @lc code=end
