#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.cn/problems/climbing-stairs/description/
#
# algorithms
# Easy (55.29%)
# Likes:    3831
# Dislikes: 0
# Total Accepted:    1.8M
# Total Submissions: 3.3M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 45
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 方法一.自低向上
        # # 1.定义状态：dp[i]表示爬到第i阶楼梯的方法数
        # dp = [0] * (n + 1)

        # # 2.确定状态转移方程
        # # dp[i] = dp[i - 1] + dp[i - 2]
        
        # # 3.初始化状态
        # dp[0] = 1
        # dp[1] = 1

        # # 4.计算状态值
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]

        # 方法二.自顶向下
        # 1.初始化备忘录
        memo = {}

        def dp(i: int) -> int:
            # 2.查备忘录，避免重复计算  
            if i in memo:
                return memo[i]
            # 3.处理边界情况
            if i <= 2:
                return i
            # 4.计算状态值
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        return dp(n)
# @lc code=end

