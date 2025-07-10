# @before-stub-for-debug-begin
from python3problem6 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
# https://leetcode.cn/problems/zigzag-conversion/description/
#
# algorithms
# Medium (53.57%)
# Likes:    2449
# Dislikes: 0
# Total Accepted:    760.7K
# Total Submissions: 1.4M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
# 
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
# 
# 请你实现这个将字符串进行指定行数变换的函数：
# 
# 
# string convert(string s, int numRows);
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
# 
# 示例 2：
# 
# 
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
# 
# 示例 3：
# 
# 
# 输入：s = "A", numRows = 1
# 输出："A"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由英文字母（小写和大写）、',' 和 '.' 组成
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 1. 暴力
        # if numRows == 1: return s
        # res = ['' for _ in range(numRows)]
        # row, flag = 0, -1
        # for c in s:
        #     res[row] += c
        #     if row == 0 or row == numRows - 1:
        #         flag = -flag
        #     row += flag
        # return ''.join(res)

        # 2. 找规律
        if numRows == 1 or numRows >= len(s):
            return s
        # 初始化 numRows 个空字符串
        rows = [''] * numRows
        current_row = 0
        step = -1
        for char in s:
            rows[current_row] += char
            # 当到达第一行或最后一行时，改变方向
            if current_row == 0 or current_row == numRows - 1:
                step = -step
            current_row += step

        return ''.join(rows)

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    print(solution.convert(s, numRows))
