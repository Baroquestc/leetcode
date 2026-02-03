#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] Transpose Matrix
#
# https://leetcode.cn/problems/transpose-matrix/description/
#
# algorithms
# Easy (69.04%)
# Likes:    294
# Dislikes: 0
# Total Accepted:    134.9K
# Total Submissions: 195.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a 2D integer array matrix, return the transpose of matrix.
# 
# The transpose of a matrix is the matrix flipped over its main diagonal,
# switching the matrix's row and column indices.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 10^5
# -10^9 <= matrix[i][j] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # 1.常规解法
        # if not matrix:
        #     return []

        # m = len(matrix)
        # n = len(matrix[0])
        # transposed = [[0] * m for _ in range(n)]

        # for i in range(m):
        #     for j in range(n):
        #         transposed[j][i] = matrix[i][j]
        
        # return transposed

        # 2. Pythonic 解法
        return list(map(list, zip(*matrix)))
# @lc code=end
