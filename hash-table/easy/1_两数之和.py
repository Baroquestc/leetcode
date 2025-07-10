#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idex, num in enumerate(nums):
            nums_dict[num] = idex
            if target-num in nums_dict:
                return [nums_dict[target-num], idex]
            nums_dict[num] = idex
        return []
# @lc code=end

