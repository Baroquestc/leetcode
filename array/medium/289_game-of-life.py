#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] Game of Life
#
# https://leetcode.cn/problems/game-of-life/description/
#
# algorithms
# Medium (77.16%)
# Likes:    671
# Dislikes: 0
# Total Accepted:    143K
# Total Submissions: 185.3K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# The board is made up of an m x n grid of cells, where each cell has an
# initial state: live (represented by a 1) or dead (represented by a 0). Each
# cell interacts with its eight neighbors (horizontal, vertical, diagonal)
# using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# Any live cell with fewer than two live neighbors dies as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# The next state of the board is determined by applying the above rules
# simultaneously to every cell in the current state of the m x n grid board. In
# this process, births and deaths occur simultaneously.
# 
# Given the current state of the board, update the board to reflect its next
# state.
# 
# Note that you do not need to return anything.
# 
# 
# Example 1:
# 
# 
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# 
# 
# Example 2:
# 
# 
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.
# 
# 
# 
# Follow up:
# 
# 
# Could you solve it in-place? Remember that the board needs to be updated
# simultaneously: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# upon the border of the array (i.e., live cells reach the border). How would
# you address these problems?
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1.基础算法
        # m, n = len(board), len(board[0])
        # # 复制一份当前棋盘
        # copy_board = [[board[i][j] for j in range(n)] for i in range(m)]

        # # 定义八个方向
        # directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # # 遍历每个细胞
        # for i in range(m):
        #     for j in range(n):
        #         # 计算周围活细胞的数量
        #         live_neighbors = 0
        #         for dx, dy in directions:
        #             ni, nj = i + dx, j + dy
        #             if 0 <= ni < m and 0 <= nj < n and copy_board[ni][nj] == 1:
        #                 live_neighbors += 1

        #         # 应用规则
        #         if copy_board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
        #             board[i][j] = 0
        #         elif copy_board[i][j] == 0 and live_neighbors == 3:
        #             board[i][j] = 1

        # 2.进阶算法
        rows, cols = len(board), len(board[0])  # 矩阵的行数和列数  
        
        # 定义所有的八个方向  
        directions = [(-1, -1), (-1, 0), (-1, 1),   
                      (0, -1),         (0, 1),   
                      (1, -1), (1, 0), (1, 1)]  
        
        # 遍历每一个格子  
        for row in range(rows):  
            for col in range(cols):  
                # 统计当前格子的活邻居数量  
                live_neighbors = 0  
                for dr, dc in directions:  # 遍历八个方向  
                    new_row, new_col = row + dr, col + dc  
                    # 检查是否在矩阵范围内，并判断是否是活细胞（考虑中间状态）
                    if 0 <= new_row < rows and 0 <= new_col < cols and (board[new_row][new_col] == 1 or board[new_row][new_col] == 2):  
                        live_neighbors += 1  
                
                # 根据规则更新状态（使用中间状态避免冲突）  
                if board[row][col] == 1:  # 当前是活细胞  
                    if live_neighbors < 2 or live_neighbors > 3:  
                        board[row][col] = 2  # 活变死  
                else:  # 当前是死细胞  
                    if live_neighbors == 3:  
                        board[row][col] = -1  # 死变活  

        # 恢复所有的中间状态到最终结果  
        for row in range(rows):  
            for col in range(cols):  
                if board[row][col] == 2:  
                    board[row][col] = 0  # 活变死  
                elif board[row][col] == -1:  
                    board[row][col] = 1  # 死变活 
# @lc code=end
