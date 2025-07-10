#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachable = 0
        n = len(nums)

        for i in range(n):
            if i > maxReachable:
                return False
            maxReachable = max(maxReachable, i + nums[i])
            if maxReachable >= n - 1:
                return True
        return False
# @lc code=end

