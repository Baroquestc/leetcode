#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.cn/problems/generate-parentheses/description/
#
# algorithms
# Medium (78.84%)
# Likes:    3845
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 1.3M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        res = []
        backtrack()
        return res
        
# @lc code=end

