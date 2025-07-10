#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode.cn/problems/longest-common-prefix/description/
#
# algorithms
# Easy (44.50%)
# Likes:    3232
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 3.2M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 
# 
# 
# 提示：
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 1. 暴力法
        # if not strs:
        #     return ""
        # # 以第一个字符串为基准
        # for i in range(len(strs[0])):
        #     for string in strs[1:]:
        #         # 如果当前字符串的长度小于第一个字符串的长度或者当前字符不等于第一个字符串的字符
        #         if i >= len(string) or string[i] != strs[0][i]:
        #             return strs[0][:i]
        # return strs[0]
        
        # 2. 分治法
        def lcp(start, end):
            if start == end:
                return strs[start]
            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]
            return lcpLeft[:minLength]
        return "" if not strs else lcp(0, len(strs) - 1)
# @lc code=end

