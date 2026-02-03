#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # 1.常规解法
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        transposed = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        
        return transposed

        # 2. Pythonic 解法
        # return list(map(list, zip(*matrix)))

# @lc code=end
