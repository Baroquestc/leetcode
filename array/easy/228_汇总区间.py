#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        left, right = 0, 1
        nums_list = []
        while right < len(nums):
            if nums[right] - nums[right - 1] != 1:
                if left == right - 1:
                    nums_list.append(str(nums[left]))
                else:
                    nums_list.append(f"{nums[left]}->{nums[right - 1]}")
                left = right
            right += 1
        
        if left == right - 1:
            nums_list.append(str(nums[left]))
        else:
            nums_list.append(f"{nums[left]}->{nums[right - 1]}")
        
        return nums_list
        
# @lc code=end

