from typing import List

#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] Number of Matching Subsequences
#
# https://leetcode.cn/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (50.93%)
# Likes:    432
# Dislikes: 0
# Total Accepted:    47.8K
# Total Submissions: 93.8K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given a string s and an array of strings words, return the number of words[i]
# that is a subsequence of s.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
# 
# 
# For example, "ace" is a subsequence of "abcde".
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s:
# "a", "acd", "ace".
# 
# 
# Example 2:
# 
# 
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    # 思路一：
    # def is_subsequence(self, word: str, s: str) -> bool:
    #     """检查word是否是s的子序列"""
    #     word_idx = 0
    #     s_idx = 0
        
    #     while word_idx < len(word) and s_idx < len(s):
    #         if word[word_idx] == s[s_idx]:
    #             word_idx += 1
    #         s_idx += 1
        
    #     return word_idx == len(word)

    # def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    #     count = 0
    #     for word in words:
    #         if self.is_subsequence(word, s):
    #             count += 1
    #     return count

    # 思路二：
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        from collections import defaultdict
        import bisect

        # 预处理s，记录每个字符出现的位置
        char_indices = defaultdict(list)
        for index, char in enumerate(s):
            char_indices[char].append(index)

        def is_subsequence(word: str) -> bool:
            """检查word是否是s的子序列"""
            current_position = -1  # 记录当前在s中的位置
            for char in word:
                if char not in char_indices:
                    return False
                # 使用二分查找找到下一个位置
                positions = char_indices[char]
                next_index = bisect.bisect_right(positions, current_position)
                if next_index == len(positions):
                    return False
                current_position = positions[next_index]
            return True

        count = sum(1 for word in words if is_subsequence(word))
        return count
# @lc code=end
