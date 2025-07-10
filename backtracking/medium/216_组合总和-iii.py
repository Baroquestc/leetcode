#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode.cn/problems/combination-sum-iii/description/
#
# algorithms
# Medium (71.54%)
# Likes:    927
# Dislikes: 0
# Total Accepted:    469.4K
# Total Submissions: 656.3K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
# 
# 
# 只使用数字1到9
# 每个数字 最多使用一次 
# 
# 
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 解释:
# 1 + 2 + 4 = 7
# 没有其他符合的组合了。
# 
# 示例 2:
# 
# 
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 解释:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# 没有其他符合的组合了。
# 
# 示例 3:
# 
# 
# 输入: k = 4, n = 1
# 输出: []
# 解释: 不存在有效的组合。
# 在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。
# 
# 
# 
# 
# 提示:
# 
# 
# 2 <= k <= 9
# 1 <= n <= 60
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 用于存储最终结果的列表
        res = []
        def backtrack(start, track, remain):
            """
            回溯函数，用于生成组合总和
            :param start: 开始的索引，确保组合中的数字是从当前索引开始选取，避免重复组合"
            ":param track: 当前已经生成的组合"
            ":param remain: 剩余需要达到目标值的差值""
            """
            # 当剩余差值为 0 且组合长度为 k 时，说明找到了一个有效的组合
            if remain == 0 and len(track) == k:
                # 使用 track[:] 进行浅拷贝，将当前组合添加到结果列表中
                res.append(track[:])
                return
            # 当剩余差值小于 0 或组合长度大于 k 时，停止递归
            if remain < 0 or len(track) > k:
                return
            # 从 start 开始遍历数字 1 到 9
            for i in range(start, 10):
                # 将当前数字添加到组合中
                track.append(i)
                # 递归调用回溯函数，更新剩余差值和开始索引
                backtrack(i + 1, track, remain - i)
                # 回溯，将当前数字从组合中移除
                track.pop()
        # 调用回溯函数，从数字 1 开始生成组合
        backtrack(1, [], n)
        # 返回最终结果列表
        return res
    
# @lc code=end

