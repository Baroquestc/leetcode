#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (75.28%)
# Likes:    1819
# Dislikes: 0
# Total Accepted:    611.3K
# Total Submissions: 812K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given the root of a binary tree, flatten the tree into a "linked list":
# 
# 
# The "linked list" should use the same TreeNode class where the right child
# pointer points to the next node in the list and the left child pointer is
# always null.
# The "linked list" should be in the same order as a pre-order traversal of the
# binary tree.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Can you flatten the tree in-place (with O(1) extra space)?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten_tree(node):
            if not node:
                return None
            
            # Flatten left and right subtrees
            left_tail = flatten_tree(node.left)
            right_tail = flatten_tree(node.right)
            
            # If there is a left subtree, we need to attach it to the right
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            
            # Return the last node in the flattened tree
            return right_tail if right_tail else left_tail if left_tail else node
        
        flatten_tree(root)

# @lc code=end
