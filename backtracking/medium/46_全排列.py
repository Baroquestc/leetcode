#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def dfs(start_index):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(start_index, len(nums)):
                if not used[i]:
                    # 选择
                    path.append(nums[i])
                    used[i] = True

                    dfs(start_index)
                    path.pop()
                    used[i] = False

        dfs(0)

        return res
# @lc code=end

