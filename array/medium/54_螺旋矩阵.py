# @before-stub-for-debug-begin
from ast import boolop
from re import L
from turtle import right
from python3problem54 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 1.方法一
        # if not matrix:
        #     return []
        
        # m, n = len(matrix), len(matrix[0])
        # top, bottom = 0, m - 1
        # left, right = 0, n - 1
        # res = []

        # while top <= bottom and left <= right:
        #     # left -> right
        #     for i in range(left, right + 1):
        #         res.append(matrix[top][i])
        #     top += 1

        #     # top -> bottom
        #     for i in range(top, bottom + 1):
        #         res.append(matrix[i][right])
        #     right -= 1

        #     # right -> left
        #     if top <= bottom:
        #         for i in range(right, left - 1, -1):
        #             res.append(matrix[bottom][i])
        #         bottom -= 1

        #     # bottom -> top
        #     if left <= right:
        #         for i in range(bottom, top - 1, -1):
        #             res.append(matrix[i][left])
        #         left += 1
        # return res

        # 2.方法二
        if not matrix:
            return []
        m, n = len(matrix),len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []

        while top <= bottom and left <= right:
            # left -> right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            # top -> bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            # right -> left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break

            # bottom -> top
            for i in range(bottom, top -1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return res
# @lc code=end

