#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i]表示第i天卖出的最大利润
        # dp[i] = max(dp[i-1], prices[i] - min(prices[0:i]))
        dp = [0] * len(prices)
        min_price = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return dp[-1]

# @lc code=end

