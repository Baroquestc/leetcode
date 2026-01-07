#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.cn/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (57.46%)
# Likes:    3996
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2.2M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 方法一：自底向上
        # # 1. 状态定义：dp[i]表示以nums[i]结尾的最长递增子序列的长度
        # dp = [1] * len(nums)
        # # 2. 状态转移方程
        # # dp[i] = max(dp[i], dp[j] + 1) if nums[j] < nums[i]
        # # 3. 初始化：dp[i] = 1
        # # 4. 遍历顺序：i从0到n-1，j从0到i-1
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)
        
        # 方法二：自顶向下
        # 1. 初始化备忘录
        memo = {}
        # 2. 定义递归函数
        def dp(i):
            # 3. 查找备忘录
            if i in memo:
                return memo[i]
            # 4. 处理边界情况
            if i == 0:
                return 1
            # 5. 状态转移方程
            max_len = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len, dp(j) + 1)
            memo[i] = max_len
            return max_len

        return max(dp(i) for i in range(len(nums)))
        
# @lc code=end
