#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (60.18%)
# Likes:    958
# Dislikes: 0
# Total Accepted:    445.1K
# Total Submissions: 739.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the zigzag level order traversal of
# its nodes' values. (i.e., from left to right, then right to left for the next
# level and alternate between).
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: [[1]]
# 
# 
# Example 3:
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
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result = []
        left_to_right = True
        while queue:
            level_size = len(queue)
            level_nodes = []
            for i in range(level_size):
                node = queue.pop(0)
                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
            left_to_right = not left_to_right
        return result
# @lc code=end

