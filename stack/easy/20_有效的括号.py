# @before-stub-for-debug-begin
from python3problem20 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode.cn/problems/valid-parentheses/description/
#
# algorithms
# Easy (44.51%)
# Likes:    4647
# Dislikes: 0
# Total Accepted:    2.1M
# Total Submissions: 4.7M
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "()"
# 
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "()[]{}"
# 
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 输入：s = "(]"
# 
# 输出：false
# 
# 
# 示例 4：
# 
# 
# 输入：s = "([])"
# 
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s 仅由括号 '()[]{}' 组成
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  
        mapping = {')': '(', '}': '{', ']': '['}  

        for char in s:  
            if char in mapping:  
                # 如果栈为空或栈顶元素不匹配，返回False  
                top_element = stack.pop() if stack else '#'  
                if mapping[char] != top_element:  
                    return False  
            else:  
                # 如果是左括号，压入栈中  
                stack.append(char)  

        # 如果栈为空，说明所有括号都匹配成功  
        return not stack 
# @lc code=end

