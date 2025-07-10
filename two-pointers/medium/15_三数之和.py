#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. 方法一
        # left, right = 0, len(nums) - 1
        # nums.sort()
        # res = []
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     left, right = i + 1, len(nums) - 1
        #     while left < right:
        #         if nums[i] + nums[left] + nums[right] == 0:
        #             res.append([nums[i], nums[left], nums[right]])
        #             while left < right and nums[left] == nums[left+1]:
        #                 left += 1
        #             while left < right and nums[right] == nums[right-1]:
        #                 right -= 1
        #             left += 1
        #             right -= 1
        #         elif nums[i] + nums[left] + nums[right] < 0:
        #             left += 1
        #         else:
        #             right -= 1
        # return res

        # 2.方法二
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return res

# @lc code=end
