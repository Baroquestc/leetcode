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
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        # 时间复杂度：O(n)
        # 空间复杂度：O(min(m, n))
        # 其中 n 是字符串的长度，m 是字符集的大小。
        # 本题中字符串由英文字母、数字、符号和空格组成，因此 m=128
        # left, right = 0, 0
        # window = {}
        # res = 0
        # while right < len(s):
        #     c = s[right]
        #     right += 1
        #     window[c] = window.get(c, 0) + 1
        #     while window[c] > 1:
        #         d = s[left]
        #         left += 1
        #         window[d] -= 1
        #     res = max(res, right - left)
        # return res

        # 优化
        # left, right = 0, 0
        # window = {}
        # res = 0
        # while right < len(s):
        #     c = s[right]
        #     right += 1
        #     window[c] = window.get(c, 0) + 1
        #     while window[c] > 1:
        #         d = s[left]
        #         left += 1
        #         window[d] -= 1
        #     res = max(res, right - left)
        # return res

        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
        
# @lc code=end
import unittest

class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """测试示例1: 包含重复字符的普通字符串"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_2(self):
        """测试示例2: 仅含有重复字符的字符串"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_example_3(self):
        """测试示例3: 普通字符串，最长子串在中间"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_empty_string(self):
        """测试空字符串"""
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_single_character(self):
        """测试单字符"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("a"), 1)

    def test_all_unique(self):
        """测试全部字符都不重复的字符串"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdefg"), 7)

    def test_repeats_at_beginning(self):
        """测试开头有重复字符的字符串"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("aabcdef"), 6)

    def test_repeats_at_end(self):
        """测试结尾有重复字符的字符串"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdeff"), 6)

    # def test_complex_string(self):
    #     """测试带有空格、数字和特殊字符的复杂字符串"""
    #     self.assertEqual(self.solution.lengthOfLongestSubstring("ab c!d@1"), 7)

    def test_repeating_pattern(self):
        """测试有重复模式的字符串"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcd"), 4)

if __name__ == '__main__':
    unittest.main()
