# @before-stub-for-debug-begin
from python3problem69 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#
# https://leetcode.cn/problems/sqrtx/description/
#
# algorithms
# Easy (38.65%)
# Likes:    1608
# Dislikes: 0
# Total Accepted:    991.7K
# Total Submissions: 2.6M
# Testcase Example:  '4'
#
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
# 
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 4
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 < x:
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1
            else:
                return mid
        return left - 1
# @lc code=end

