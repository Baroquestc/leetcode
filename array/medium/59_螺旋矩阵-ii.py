#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 方法一：模拟
        if not n:
            return []

        left, right = 0, n - 1
        top, bottom = 0, n - 1
        res = []
        matrix = [[0] * n for _ in range(n)]
        num = 1

        while left <= right and top <= bottom:
            # left -> right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            if top > bottom:
                break

            # top -> bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            if left > right:
                break

            # right -> left
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            if top > bottom:
                break

            # bottom -> top
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            if left > right:
                break

        return matrix
# @lc code=end
