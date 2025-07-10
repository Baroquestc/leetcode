# @before-stub-for-debug-begin
from python3problem205 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# https://leetcode.cn/problems/isomorphic-strings/description/
#
# algorithms
# Easy (49.74%)
# Likes:    747
# Dislikes: 0
# Total Accepted:    314.7K
# Total Submissions: 632.6K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t ，判断它们是否是同构的。
# 
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
# 
# 
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
# 
# 
# 
# 示例 1:
# 
# 
# 输入：s = "egg", t = "add"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "foo", t = "bar"
# 输出：false
# 
# 示例 3：
# 
# 
# 输入：s = "paper", t = "title"
# 输出：true
# 
# 
# 
# 提示：
# 
# 
# 
# 
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s 和 t 由任意有效的 ASCII 字符组成
# 
# 
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if len(s) != len(t): return False
        # s2t= {}
        # for char_s, char_t in zip(s,t):
        #     if char_s in s2t and s2t[char_s] != char_t:
        #         return False
        #     if char_s not in s2t:
        #         s2t[char_s] = char_t
        # return True

        if len(s) != len(t):
            return False
        s2t = {}
        t2s = {}
        for s_str, t_str in zip(s, t):
            if s_str in s2t:
                if s2t[s_str] != t_str:
                    return False
            elif t_str in t2s:
                if t2s[t_str] != s_str:
                    return False
            else:
                s2t[s_str] = t_str
                t2s[t_str] = s_str
        return True
# @lc code=end
