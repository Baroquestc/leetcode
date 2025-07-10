#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        num_len = len(num)
        if num_len % 2 == 0:
            return (num[num_len // 2 - 1] + num[num_len // 2]) / 2
        else:
            return num[num_len // 2]
# @lc code=end

