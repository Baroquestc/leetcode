#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (63.03%)
# Likes:    620
# Dislikes: 0
# Total Accepted:    322.4K
# Total Submissions: 511.4K
# Testcase Example:  '[4,2,6,1,3]'
#
# Given the root of a Binary Search Tree (BST), return the minimum absolute
# difference between the values of any two different nodes in the tree.
# 
# 
# Example 1:
# 
# 
# Input: root = [4,2,6,1,3]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 10^4].
# 0 <= Node.val <= 10^5
# 
# 
# 
# Note: This question is the same as 783:
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.sort()
        min_diff = float('inf')
        for i in range(1, len(result)):
            min_diff = min(min_diff, result[i] - result[i-1])
        return min_diff
        
# @lc code=end

