#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}
        for index, num in enumerate(nums):
            if num in nums_dict and index - nums_dict[num] <= k:
                return True
            nums_dict[num] = index
        return False
        
# @lc code=end
