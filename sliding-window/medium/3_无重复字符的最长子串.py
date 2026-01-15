# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (40.49%)
# Likes:    10495
# Dislikes: 0
# Total Accepted:    3.2M
# Total Submissions: 7.9M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 5 * 10^4
# s 由英文字母、数字、符号和空格组成
# 
# 
#

# @lc code=start
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # 滑动窗口
#         # 时间复杂度：O(n)
#         # 空间复杂度：O(min(m, n))
#         # 其中 n 是字符串的长度，m 是字符集的大小。
#         # 本题中字符串由英文字母、数字、符号和空格组成，因此 m=128
#         # left, right = 0, 0
#         # window = {}
#         # res = 0
#         # while right < len(s):
#         #     c = s[right]
#         #     right += 1
#         #     window[c] = window.get(c, 0) + 1
#         #     while window[c] > 1:
#         #         d = s[left]
#         #         left += 1
#         #         window[d] -= 1
#         #     res = max(res, right - left)
#         # return res

#         # 优化
#         # left, right = 0, 0
#         # window = {}
#         # res = 0
#         # while right < len(s):
#         #     c = s[right]
#         #     right += 1
#         #     window[c] = window.get(c, 0) + 1
#         #     while window[c] > 1:
#         #         d = s[left]
#         #         left += 1
#         #         window[d] -= 1
#         #     res = max(res, right - left)
#         # return res

#         seen = set()
#         left = 0
#         max_length = 0

#         for right in range(len(s)):
#             while s[right] in seen:
#                 seen.remove(s[left])
#                 left += 1
#             seen.add(s[right])
#             max_length = max(max_length, right - left + 1)

#         return max_length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 创建一个字典来记录当前窗口中每个字符的出现次数
        char_count = {}
        left = 0  # 滑动窗口的左边界
        res = 0   # 记录最长无重复子串的长度
    
        # 遍历字符串，right作为滑动窗口的右边界
        for right in range(len(s)):
            # 获取当前右边界指向的字符
            char_right = s[right]
            # 更新该字符在窗口中的计数
            char_count[char_right] = char_count.get(char_right, 0) + 1
            
            # 如果当前字符在窗口中出现次数大于1，说明有重复字符
            # 需要从左侧移动窗口，直到重复字符被移出窗口
            while char_count[char_right] > 1:
                # 获取左边界指向的字符
                char_left = s[left]
                # 减少该字符在窗口中的计数
                char_count[char_left] -= 1
                # 左边界右移，缩小窗口
                left += 1
            
            # 更新最长无重复子串的长度
            # 当前窗口长度为 right - left + 1
            res = max(res, right - left + 1)
        
        return res  # 返回最长无重复子串的长度
# @lc code=end