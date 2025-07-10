# @before-stub-for-debug-begin
from python3problem205 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.cn/problems/isomorphic-strings/description/
#
# algorithms
# Easy (50.13%)
# Likes:    781
# Dislikes: 0
# Total Accepted:    349.1K
# Total Submissions: 696.3K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.
# 
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# 
# Output: true
# 
# Explanation:
# 
# The strings s and t can be made identical by:
# 
# 
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# 
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# 
# Output: false
# 
# Explanation:
# 
# The strings s and t can not be made identical as 'o' needs to be mapped to
# both 'a' and 'r'.
# 
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# 
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.
# 
# 
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s2t = {}
        t2s = {}
        for s_char, t_char in zip(s, t):
            if s_char in s2t:
                if s2t[s_char] != t_char:
                    return False
            else:
                if t2s[t_char] != s_char:
                    return False
            s2t[s_char] = t_char
            t2s[t_char] = s_char
        return True
# @lc code=end

