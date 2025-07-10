from typing import List
#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode.cn/problems/combination-sum-ii/description/
#
# algorithms
# Medium (60.00%)
# Likes:    1663
# Dislikes: 0
# Total Accepted:    616.2K
# Total Submissions: 1M
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 
# 注意：解集不能包含重复的组合。 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 示例 2:
# 
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# 提示:
# 
# 
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 用于存储最终的组合结果
        res = []
        # 用于存储当前正在构建的组合
        track = []
        # 对候选数字列表进行排序，方便后续去重操作
        candidates.sort()

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
                # 如果当前数字大于目标值，后续数字只会更大，直接跳出循环
                if candidates[i] > target:
                    break
                # 跳过重复的数字，避免生成重复的组合
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # 将当前数字加入到组合中
                track.append(candidates[i])
                # 递归调用 backtrack 函数，继续生成组合，由于每个数字只能使用一次，所以下一次递归的起始索引为 i + 1
                backtrack(i + 1, track, remain - candidates[i])
                # 回溯操作，移除最后一个添加的数字，以便尝试其他可能的组合
                track.pop()

        # 从索引 0 开始，初始组合为空列表，剩余差值为目标值
        backtrack(0, track, target)

        # 返回最终结果
        return res
        
# @lc code=end
import unittest

class TestCombinationSum2(unittest.TestCase):

    def test_combinationSum2(self):
        # 测试用例 1：正常情况
        candidates1 = [10, 1, 2, 7, 6, 1, 5]
        target1 = 8
        expected1 = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        self.assertEqual(Solution().combinationSum2(candidates1, target1), expected1)

        # 测试用例 2：没有满足条件的组合
        candidates2 = [2, 3, 6, 6]
        target2 = 10
        expected2 = []
        self.assertEqual(Solution().combinationSum2(candidates2, target2), expected2)

        # 测试用例 3：所有数字都相同
        candidates3 = [1, 1, 1, 1, 1]
        target3 = 2
        expected3 = [[1, 1]]
        self.assertEqual(Solution().combinationSum2(candidates3, target3), expected3)

if __name__ == '__main__':
    unittest.main()