#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
# https://leetcode.cn/problems/word-pattern/description/
#
# algorithms
# Easy (44.93%)
# Likes:    685
# Dislikes: 0
# Total Accepted:    213.4K
# Total Submissions: 475K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
# 
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。
# 
# 
# 
# 示例1:
# 
# 
# 输入: pattern = "abba", s = "dog cat cat dog"
# 输出: true
# 
# 示例 2:
# 
# 
# 输入:pattern = "abba", s = "dog cat cat fish"
# 输出: false
# 
# 示例 3:
# 
# 
# 输入: pattern = "aaaa", s = "dog cat cat dog"
# 输出: false
# 
# 
# 
# 提示:
# 
# 
# 1 <= pattern.length <= 300
# pattern 只包含小写英文字母
# 1 <= s.length <= 3000
# s 只包含小写英文字母和 ' '
# s 不包含 任何前导或尾随对空格
# s 中每个单词都被 单个空格 分隔
# 
# 
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 方法1： 哈希表
        # s_list = s.split(' ')
        # if len(pattern) != len(s_list):
        #     return False
        # pattern_dict = {}
        # for i in range(len(pattern)):
        #     if pattern[i] in pattern_dict:
        #         if pattern_dict[pattern[i]] != s_list[i]:
        #             return False
        #     else:
        #         if s_list[i] in pattern_dict.values():
        #             return False
        #         pattern_dict[pattern[i]] = s_list[i]
        # return True
        
        # 方法2： 哈希表， 优化
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False
        word2char = {}
        char2word = {}
        for char, word in zip(pattern, s_list):
            if char in char2word:
                if char2word[char] != word:
                    return False
            else:
                if word in word2char:
                    return False
                word2char[word] = char
                char2word[char] = word
        return True 
        
# @lc code=end

