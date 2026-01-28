#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1.双指针法1
        # if not nums:
        #     return

        # left, right = 0, 0
        # while left <= right and right < len(nums):
        #     if nums[right]:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        #     right += 1

        # return nums

        # 2.双指针法2
        if not nums:
            return

        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left] = nums[right]
                left += 1
        
        for i in range(left, len(nums)):
            nums[i] = 0
# @lc code=end

