#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

from typing import List
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        N = len(digits)
        if (N == 0):
            return []
        mp = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7' : 'pqrs', '8': 'tuv', '9':'wxyz'}

        ans = []
        for i in range (N):
            if (i == 0):
                for c in mp[digits[i]]:
                    ans.append(c)
            else:
                tmp = []
                for c in mp[digits[i]]:
                    for s in ans:
                        tmp.append(s + c)
                ans = tmp

        return ans
# @lc code=end

print (Solution().letterCombinations("23"))
