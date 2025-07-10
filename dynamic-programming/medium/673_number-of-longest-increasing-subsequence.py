#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#
# https://leetcode.cn/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (45.54%)
# Likes:    948
# Dislikes: 0
# Total Accepted:    124K
# Total Submissions: 272.2K
# Testcase Example:  '[1,3,5,4,7]'
#
# Given an integer array nums, return the number of longest increasing
# subsequences.
# 
# Notice that the sequence has to be strictly increasing.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1,
# 3, 5, 7].
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there
# are 5 increasing subsequences of length 1, so output 5.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2000
# -10^6 <= nums[i] <= 10^6
# The answer is guaranteed to fit inside a 32-bit integer.
# 
# 
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        
        max_len = max(dp)
        return sum(count[i] for i in range(n) if dp[i] == max_len)
# @lc code=end

