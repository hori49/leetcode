#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtracking(S, left, right):
            if len(S) == 2*n:
                ans.append(S)
                return

            if left < n:
                backtracking(S+'(', left+1, right)

            if right < left:
                backtracking(S+')', left, right+1)

        backtracking('', 0, 0)
        return ans
# @lc code=end

print (Solution().generateParenthesis(3))