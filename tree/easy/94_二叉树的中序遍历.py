# @before-stub-for-debug-begin
import queue
from python3problem94 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 1.递归法
        # if not root:
        #     return []
        
        # res = []

        # def inorder(root):
        #     if root:
        #         inorder(root.left)
        #         res.append(root.val)
        #         inorder(root.right)

        # inorder(root)
        # return res

        # 2.迭代法
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)

                stack.append(node)
                stack.append(None)

                if node.left:
                    stack.append(node.left)
            else:
                node = stack.pop()
                res.append(node.val)

        return res
                
                
# @lc code=end

