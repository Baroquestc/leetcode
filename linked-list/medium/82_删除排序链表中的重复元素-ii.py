#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (54.82%)
# Likes:    1340
# Dislikes: 0
# Total Accepted:    503.5K
# Total Submissions: 918.5K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
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
        # 1.递归
        # if not head or not head.next:
        #     return head
        # if head.val != head.next.val:
        #     head.next = self.deleteDuplicates(head.next)
        #     return head
        # else:
        #     while head.next and head.val == head.next.val:
        #         head = head.next
        #     return self.deleteDuplicates(head.next)

        # 2.双指针
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        pre = dummy
        cur = head
        while cur and cur.next:
            if cur.val != cur.next.val:
                pre = pre.next
                cur = cur.next
            else:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
                cur = cur.next
        return dummy.next

# @lc code=end
