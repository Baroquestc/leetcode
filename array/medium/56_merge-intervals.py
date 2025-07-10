# @before-stub-for-debug-begin
from python3problem56 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.cn/problems/merge-intervals/description/
#
# algorithms
# Medium (51.26%)
# Likes:    2540
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.2M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1.way1
        # if not intervals:
        #     return []
        # # 1. sort the intervals by the start value
        # intervals.sort(key=lambda x: x[0])
        
        # res = [intervals[0]]
        # for i in range(1, len(intervals)):
        #     # 2. if the start value of the current interval is less than the end value of the last interval in res, merge the two intervals
        #     if intervals[i][0] <= res[-1][1]:
        #         res[-1][1] = max(res[-1][1], intervals[i][1])
        #     else:
        #         res.append(intervals[i])
        # return res

        # 2.way2
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            pre = res[-1]
            cur = intervals[i]

            if pre[1] < cur[0]:
                res.append(cur)
            else:
                res[-1][1] = max(pre[1], cur[1])
                    
        return res

# @lc code=end

