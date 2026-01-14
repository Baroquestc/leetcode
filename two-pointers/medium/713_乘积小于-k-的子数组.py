#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#
# https://leetcode.cn/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (54.01%)
# Likes:    890
# Dislikes: 0
# Total Accepted:    173.2K
# Total Submissions: 320.7K
# Testcase Example:  '[10,5,2,6]\n100'
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2]、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3], k = 0
# 输出：0
# 
# 
# 
# 提示: 
# 
# 
# 1 <= nums.length <= 3 * 10^4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 方法1
        # if k <= 1:
        #     return 0
        # product = 1
        # left = 0
        # result = 0
        # for right in range(len(nums)):
        #     product *= nums[right]
        #     while product >= k:
        #         product /= nums[left]
        #         left += 1
        #     result += right - left + 1
        # return result

        # 方法2
        prod = 1
        ans = 0
        left = 0
        
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans
# @lc code=end

