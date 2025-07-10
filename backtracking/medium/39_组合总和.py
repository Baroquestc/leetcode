#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode.cn/problems/combination-sum/description/
#
# algorithms
# Medium (73.65%)
# Likes:    3003
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 1.6M
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target
# 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
# 
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
# 
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
# 
# 示例 2：
# 
# 
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
# 
# 示例 3：
# 
# 
# 输入: candidates = [2], target = 1
# 输出: []
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# candidates 的所有元素 互不相同
# 1 <= target <= 40
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 用于存储最终结果的列表
        res = []
        def backtrack(start, track, remain):
            """
            回溯函数，用于生成组合总和
            :param start: 开始的索引，确保组合中的数字是从当前索引开始选取，避免重复组合
            :param track: 当前已经生成的组合
            :param remain: 剩余需要达到目标值的差值
            """
            # 当剩余差值为 0 时，说明找到了一个有效的组合
            if remain == 0:
                # 使用 track[:] 进行浅拷贝，将当前组合添加到结果列表中
                res.append(track[:])
                return
            # 当剩余差值小于 0 时，说明当前组合的和已经超过了目标值，停止递归
            if remain < 0:
                return
            # 从 start 开始遍历 candidates 列表
            for i in range(start, len(candidates)):
                # 将当前数字加入到组合中
                track.append(candidates[i])
                # 递归调用 backtrack 函数，继续生成组合，由于数字可以重复使用，所以下一次递归的起始索引仍为 i
                backtrack(i, track, remain - candidates[i])
                # 回溯操作，移除最后一个添加的数字，以便尝试其他可能的组合
                track.pop()
        # 从索引 0 开始，初始组合为空列表，剩余差值为目标值
        backtrack(0, [], target)
        # 返回最终结果
        return res
# @lc code=end

import unittest

class TestCombinationSum(unittest.TestCase):

    def test_combinationSum(self):
        # 测试用例 1：目标值为 7，候选数字为 [2,3,6,7]
        candidates1 = [2,3,6,7]
        target1 = 7
        expected1 = [[2,2,3],[7]]
        self.assertEqual(Solution().combinationSum(candidates1, target1), expected1)

        # 测试用例 2：目标值为 5，候选数字为 [2,3,5]
        candidates2 = [2,3,5]
        target2 = 5
        expected2 = [[2,3],[5]]
        self.assertEqual(Solution().combinationSum(candidates2, target2), expected2)

        # 测试用例 3：目标值为 0，候选数字为 [1,2,3]
        candidates3 = [1,2,3]
        target3 = 0
        expected3 = [[]]
        self.assertEqual(Solution().combinationSum(candidates3, target3), expected3)

if __name__ == '__main__':
    unittest.main()
