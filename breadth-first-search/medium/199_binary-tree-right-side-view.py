#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.cn/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (70.51%)
# Likes:    1196
# Dislikes: 0
# Total Accepted:    600.2K
# Total Submissions: 850.9K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,5,null,4]
# 
# Output: [1,3,4]
# 
# Explanation:
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,4,null,null,null,5]
# 
# Output: [1,3,4,5]
# 
# Explanation:
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: root = [1,null,3]
# 
# Output: [1,3]
# 
# 
# Example 4:
# 
# 
# Input: root = []
# 
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        right_side = []
        while queue:
            right_side.append(queue[-1].val)
            next_queue = []
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return right_side
        
# @lc code=end

