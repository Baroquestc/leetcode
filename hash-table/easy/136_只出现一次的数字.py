#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = {}
        for index, num in enumerate(nums):
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        for id, num in nums_dict.items():
            if num == 1:
                return id
# @lc code=end

