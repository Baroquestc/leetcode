#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode.cn/problems/word-search/description/
#
# algorithms
# Medium (48.56%)
# Likes:    1963
# Dislikes: 0
# Total Accepted:    652.3K
# Total Submissions: 1.3M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCCED"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "SEE"
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCB"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == board.length
# n = board[i].length
# 1 
# 1 
# board 和 word 仅由大小写英文字母组成
# 
# 
# 
# 
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
# 
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 用于存储最终结果的列表
        res = []
        # 用于存储当前路径上的字符
        track = []
        # 用于标记访问过的单元格
        visited = set()
        # 定义四个方向的偏移量，用于在网格中进行上下左右的移动
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # 获取网格的行数和列数
        m, n = len(board), len(board[0])
        def backtrack(i, j, track):
            """
            回溯函数，用于搜索网格中的单词
            :param i: 当前单元格的行索引"
            ":param j: 当前单元格的列索引"
            ":param track: 当前路径上的字符列表"
            """
            # 如果当前路径上的字符列表长度等于单词的长度，说明找到了一个完整的单词
            if len(track) == len(word):
                # 将当前路径上的字符列表转换为字符串，并添加到结果列表中
                res.append(''.join(track))
                return
            # 遍历四个方向的偏移量
            for di, dj in directions:
                # 计算下一个单元格的行索引和列索引
                ni, nj = i + di, j + dj
                # 如果下一个单元格的行索引和列索引都在网格范围内，并且该单元格未被访问过
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    # 将下一个单元格的字符添加到当前路径上的字符列表中
                    track.append(board[ni][nj])
                    # 将下一个单元格标记为已访问
                    visited.add((ni, nj))
                    # 递归调用回溯函数，继续搜索下一个字符
                    backtrack(ni, nj, track)
                    # 回溯，将下一个单元格从当前路径上的字符列表中移除
                    track.pop()
                    # 回溯，将下一个单元格从已访问集合中移除
                    visited.remove((ni, nj))
        # 遍历网格中的每个单元格
        for i in range(m):
            for j in range(n):
                # 如果当前单元格的字符与单词的第一个字符相同
                if board[i][j] == word[0]:
                    # 将当前单元格的字符添加到当前路径上的字符列表中
                    track.append(board[i][j])
                    # 将当前单元格标记为已访问
                    visited.add((i, j))
                    # 递归调用回溯函数，继续搜索下一个字符
                    backtrack(i, j, track)
                    # 回溯，将当前单元格从当前路径上的字符列表中移除
                    track.pop()
                    # 回溯，将当前单元格从已访问集合中移除
                    visited.remove((i, j))
        # 如果结果列表不为空，说明找到了一个完整的单词，返回 True；否则，返回 False
        return True if res else False
    
# @lc code=end
