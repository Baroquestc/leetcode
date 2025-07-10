#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode.cn/problems/group-anagrams/description/
#
# algorithms
# Medium (69.39%)
# Likes:    2142
# Dislikes: 0
# Total Accepted:    961.5K
# Total Submissions: 1.4M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 
# 示例 2:
# 
# 
# 输入: strs = [""]
# 输出: [[""]]
# 
# 
# 示例 3:
# 
# 
# 输入: strs = ["a"]
# 输出: [["a"]]
# 
# 
# 
# 提示：
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] 仅包含小写字母
# 
# 
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def str_dict(str_word):
            str_dict = {}
            for word in str_word:
                if word in str_dict:
                    str_dict[word] += 1
                else:
                    str_dict[word] = 1
            return str_dict
        
        str_dict_dict = {}
        for str_word in strs:
            str_dict = str_dict(str_word)
            str_dict_str = str(str_dict)
            if str_dict_str in str_dict_dict:
                str_dict_dict[str_dict_str].append(str_word)
            else:
                str_dict_dict[str_dict_str] = [str_word]
        return list(str_dict_dict.values())

# @lc code=end

