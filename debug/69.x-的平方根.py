#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        left, right = 1, x
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid + 1
                
        return left - 1

# @lc code=end

