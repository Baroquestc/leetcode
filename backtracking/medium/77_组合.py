#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode.cn/problems/combinations/description/
#
# algorithms
# Medium (77.56%)
# Likes:    1747
# Dislikes: 0
# Total Accepted:    860.6K
# Total Submissions: 1.1M
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 
# 你可以按 任何顺序 返回答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4, k = 2
# 输出：
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 示例 2：
# 
# 
# 输入：n = 1, k = 1
# 输出：[[1]]
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 用于存储最终结果的列表
        res = []
        def backtrack(start, track):
            """
            回溯函数，用于生成组合
            :param start: 开始的数字，确保组合中的数字是递增的
            :param track: 当前已经生成的组合
            """
            # 当当前组合的长度等于 k 时，将其添加到结果列表中
            if len(track) == k:
                # 注意这里要使用 track[:] 进行浅拷贝，避免后续修改影响结果
                res.append(track[:])
                return
            
            # 从 start 开始遍历到 n，尝试将每个数字加入到当前组合中
            for i in range(start, n+1):
                # 将当前数字加入到组合中
                track.append(i)
                # 递归调用 backtrack 函数，继续生成组合，起始数字为 i+1
                backtrack(i+1, track)
                # 回溯操作，移除最后一个添加的数字，以便尝试其他可能的组合
                track.pop()
        # 从数字 1 开始，初始组合为空列表
        backtrack(1, [])

        # 返回最终结果
        return res
# @lc code=end

import unittest

class TestSolution(unittest.TestCase):

    def test_combine(self):
        # 测试用例 1：n=4，k=2
        n1 = 4
        k1 = 2
        expected1 = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        self.assertEqual(Solution().combine(n1, k1), expected1)

        # 测试用例 2：n=5，k=3
        n2 = 5
        k2 = 3
        expected2 = [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]
        self.assertEqual(Solution().combine(n2, k2), expected2)

        # 测试用例 3：n=1，k=1
        n3 = 1
        k3 = 1
        expected3 = [[1]]
        self.assertEqual(Solution().combine(n3, k3), expected3)
        
if __name__ == '__main__':
    unittest.main()