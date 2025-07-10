#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        str_n = str(bin(n)[2:])
        return str_n.count('1')
# @lc code=end

