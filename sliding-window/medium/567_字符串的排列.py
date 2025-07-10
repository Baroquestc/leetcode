#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode.cn/problems/permutation-in-string/description/
#
# algorithms
# Medium (45.56%)
# Likes:    1040
# Dislikes: 0
# Total Accepted:    309.5K
# Total Submissions: 679.1K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。如果是，返回 true ；否则，返回 false 。
# 
# 换句话说，s1 的排列之一是 s2 的 子串 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
# 
# 
# 示例 2：
# 
# 
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 和 s2 仅包含小写字母
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1.滑动窗口
        import collections
        need = collections.Counter(s1)
        print(need)
        window = collections.Counter()
        left, right = 0, 0
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while right - left >= len(s1):
                # 在这里判断是否找到了合法的子串
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False

        """
        # 2.暴力法
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False
        dict_s1 = Counter(s1)
        for i in range(len_s2 - len_s1 + 1):
            dict_s2 = Counter(s2[i:i+len_s1])
            if dict_s1 == dict_s2:
                return True
        return False
        """
# @lc code=end

