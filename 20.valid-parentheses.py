#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        N = len(s)
        stack = []

        for i in range(N):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if s[i] == ")" and stack[-1] != "(":
                    return False
                if s[i] == "}" and stack[-1] != "{":
                    return False
                if s[i] == "]" and stack[-1] != "[":
                    return False
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False

# @lc code=end

