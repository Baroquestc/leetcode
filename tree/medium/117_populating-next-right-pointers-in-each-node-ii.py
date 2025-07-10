#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (71.60%)
# Likes:    914
# Dislikes: 0
# Total Accepted:    318K
# Total Submissions: 444.1K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# Given a binary tree
# 
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow-up:
# 
# 
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not
# count as extra space for this problem.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:  
    def connect(self, root: 'Node') -> 'Node':  
        """  
        使用 O(1) 空间复杂度连接二叉树的 next 指针 (非完美二叉树)  
        """  
        if not root:  
            return None  

        # curr 指向当前处理层的某个节点  
        curr = root  

        while curr:  # 当 curr 存在时，表示当前层还有节点需要处理，或者下一层需要被构建  
            
            # dummy 是下一层的虚拟头节点，方便处理头节点连接  
            # tail 用于在下一层构建 next 链表  
            dummy = Node(0)  # 创建一个哨兵节点  
            tail = dummy     # tail 指向下一层链表的末尾  

            # 遍历当前层 (通过已经建立好的 next 指针)  
            while curr:  
                # 如果当前节点有左孩子，将其连接到下一层链表的末尾  
                if curr.left:  
                    tail.next = curr.left  
                    tail = tail.next  # 更新 tail  
                
                # 如果当前节点有右孩子，将其连接到下一层链表的末尾  
                if curr.right:  
                    tail.next = curr.right  
                    tail = tail.next # 更新 tail  

                # 移动到当前层的下一个节点  
                curr = curr.next   
            
            # 当前层遍历完毕，下一层链表已通过 dummy 和 tail 构建完成  
            # 将 curr 指向下一层的起始节点 (dummy.next)  
            curr = dummy.next   

        return root  
        
# @lc code=end

