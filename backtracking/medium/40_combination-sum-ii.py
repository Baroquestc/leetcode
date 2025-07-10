#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.cn/problems/combination-sum-ii/description/
#
# algorithms
# Medium (60.03%)
# Likes:    1675
# Dislikes: 0
# Total Accepted:    626.7K
# Total Submissions: 1M
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note: The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# Constraints:
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
        candidates.sort()
        result = []
        self.backtrack(candidates, target, 0, [], result)
        return result
    def backtrack(self, candidates, target, start, path, result):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            self.backtrack(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)
            
# @lc code=end
