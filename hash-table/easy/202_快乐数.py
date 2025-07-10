# @before-stub-for-debug-begin
from python3problem202 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total = 0
            while number:
                digit = number % 10
                total += digit ** 2
                number //= 10
            return total
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1

# @lc code=end
