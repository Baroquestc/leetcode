#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(start_index):
            res.append(path[:])

            # 选择
            for i in range(start_index, len(nums)):
                # 选择
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)

        return res
# @lc code=end

