# @before-stub-for-debug-begin
from python3problem17 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (61.35%)
# Likes:    3026
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# 示例 2：
# 
# 
# 输入：digits = ""
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：digits = "2"
# 输出：["a","b","c"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。
# 
# 
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        def backtrack(digits, path):
            if not digits:
                res.append(path)
                return
            for c in dic[digits[0]]:
                backtrack(digits[1:], path+c)
        backtrack(digits, '')
        return res
    
# @lc code=end
