#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid//col][mid%col] == target:
                return True
            elif matrix[mid//col][mid%col] > target:
                right = mid
            else:
                left = mid + 1
        return False
# @lc code=end

