# @before-stub-for-debug-begin
from python3problem149 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        n = len(points)
        if n <= 2:
            return n
        res = 0
        for i in range(n):
            if res >= n - i or res > n // 2:
                break
            dic = {}
            for j in range(i + 1, n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if x == 0:
                    y = 1
                elif y == 0:
                    x = 1
                else:
                    if y < 0:
                        x, y = -x, -y
                    gcdXY = gcd(abs(x), abs(y))
                    x //= gcdXY
                    y //= gcdXY
                if (x, y) in dic:
                    dic[(x, y)] += 1
                else:
                    dic[(x, y)] = 1
            for _, num in dic.items():
                res = max(res, num + 1)
        return res

# @lc code=end

