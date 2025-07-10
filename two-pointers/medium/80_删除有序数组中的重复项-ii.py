# @before-stub-for-debug-begin
from python3problem80 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针
        if len(nums) <= 2:
            return len(nums)
        left, right = 2, 2
        while left <= right and right < len(nums):
            if nums[left-2] != nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left

# @lc code=end
