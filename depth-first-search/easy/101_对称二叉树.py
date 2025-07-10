#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode.cn/problems/symmetric-tree/description/
#
# algorithms
# Easy (61.68%)
# Likes:    2880
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
# 
# 
# 
# 
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 1.递归
        def isSymmetric(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return isSymmetric(left.left, right.right) and isSymmetric(left.right, right.left)
        return isSymmetric(root.left, root.right)
        
        # 2.迭代
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True
# @lc code=end

