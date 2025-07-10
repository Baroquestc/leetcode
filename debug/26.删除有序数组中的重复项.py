#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        left, right = 1, 1
        while right < len(nums):
            if nums[left - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
        
# @lc code=end

