#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index, num in enumerate(nums):
            if target - nums[index] in num_dict:
                return [index, num_dict[target-num]]
            else:
                num_dict[num] = index
        return []
# @lc code=end
