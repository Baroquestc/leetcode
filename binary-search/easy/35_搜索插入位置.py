#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 1.二分查找
        # if not nums:
        #     return 0
        # left, right = 0, len(nums)-1
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         return mid
        # return left

        # 2.哈希表
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
            if target in dic:
                return dic[target]
            if num > target:
                return i
        return len(nums)

# @lc code=end

