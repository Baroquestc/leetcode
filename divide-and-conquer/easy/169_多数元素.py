#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode.cn/problems/majority-element/description/
#
# algorithms
# Easy (66.60%)
# Likes:    2345
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,2,3]
# 输出：3
# 
# 示例 2：
# 
# 
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
# 
# 
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        len_nums = len(nums)
        nums_dict = {}
        for i in range(len_nums):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
            if nums_dict[nums[i]] > len_nums // 2:
                return nums[i]
        return -1
# @lc code=end

