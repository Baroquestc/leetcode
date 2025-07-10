#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (38.96%)
# Likes:    7479
# Dislikes: 0
# Total Accepted:    1.9M
# Total Submissions: 4.8M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的 回文 子串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbbd"
# 输出："bb"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        res = ''
        for word in range(len(s)):
            s1 = palindrome(s, word, word)
            s2 = palindrome(s, word, word+1)
            res = s1 if len(res) < len(s1) else res
            res = s2 if len(res) < len(s2) else res
        return res
# @lc code=end

