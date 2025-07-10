#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (78.30%)
# Likes:    1919
# Dislikes: 0
# Total Accepted:    1.5M
# Total Submissions: 2M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树 root ，返回其最大深度。
# 
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,null,2]
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数量在 [0, 10^4] 区间内。
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1.递归
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # 2.迭代
        if not root:
            return 0
        queue = [root]
        max_depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_depth += 1
        return max_depth
    
# @lc code=end

