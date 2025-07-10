# @before-stub-for-debug-begin
from python3problem49 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1.方法1
        # def get_str_dict(word):
        #     str_dict = {}
        #     for char in word:
        #         if char in str_dict:
        #             str_dict[char] += 1
        #         else:
        #             str_dict[char] = 1
        #     return str_dict
        
        # anagrams = {}
        # for word in strs:
        #     str_dict = get_str_dict(word)
        #     key = tuple(sorted(str_dict.items()))
        #     if key in anagrams:
        #         anagrams[key].append(word)
        #     else:
        #         anagrams[key] = [word]
        # return list(anagrams.values())
        
        # 2.方法2
        anagrams = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return list(anagrams.values())
        
# @lc code=end

