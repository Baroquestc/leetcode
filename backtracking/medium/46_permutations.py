# @before-stub-for-debug-begin
from python3problem46 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.cn/problems/permutations/description/
#
# algorithms
# Medium (80.36%)
# Likes:    3105
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0)
        return res
# @lc code=end

