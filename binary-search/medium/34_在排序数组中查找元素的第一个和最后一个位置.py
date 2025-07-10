# @before-stub-for-debug-begin
from python3problem34 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 1.递归
        # def binarySearch(nums, target, lower):
        #     left, right = 0, len(nums)
        #     while left < right:
        #         mid = left + (right - left) // 2
        #         if nums[mid] > target or (lower and nums[mid] >= target):
        #             right = mid
        #         else:
        #             left = mid + 1
        #     return left
        # leftIndex = binarySearch(nums, target, True)
        # if leftIndex == len(nums) or nums[leftIndex] != target:
        #     return [-1, -1]
        # return [leftIndex, binarySearch(nums, target, False) - 1]
        
        # 2.二分查找法
        def left_bound(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            return left
        def right_bound(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            return left - 1
            
        left = left_bound(nums, target)
        right = right_bound(nums, target)
        if left <= right:
            return [left, right]
        return [-1, -1]
# @lc code=end

