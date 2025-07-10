#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 双指针
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == s[j]:
                i += 1
            j += 1
        return i == len(s)    

# @lc code=end

