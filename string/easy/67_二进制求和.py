# @before-stub-for-debug-begin
from python3problem67 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        # 1.内置函数
        a_int = int(a, 2)
        b_int = int(b, 2)
        return bin(a_int + b_int)[2:]
        """

        # 2.模拟进位法
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            num1 = int(a[i]) if i >= 0 else 0
            num2 = int(b[j]) if j >= 0 else 0
            total = num1 + num2 + carry
            res.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1
        return ''.join(res[::-1])

# @lc code=end
