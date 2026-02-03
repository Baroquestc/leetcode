#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # 1. 先翻转再取反
        # for row in image:
        #     row.reverse()
        #     for j in range(len(row)):
        #         row[j] = 1 - row[j]
        # return image

        # 2. 一次遍历完成翻转和取反
        n = len(image)
        for row in image:
            for j in range((n + 1) // 2):
                row[j], row[n - 1 - j] = 1 - row[n - 1 - j], 1 - row[j]
        return image  

# @lc code=end

