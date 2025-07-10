#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxReachable = 0
        steps = 0
        end = 0

        for i in range(n - 1):
            maxReachable = max(maxReachable, i + nums[i])
            if i == end:
                end = maxReachable
                steps += 1
        return steps
    
# @lc code=end
