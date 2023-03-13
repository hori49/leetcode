#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while (columnNumber > 0):
            remainder = columnNumber % 26
            if (remainder == 0):
                remainder = 26
            char = chr(ord('A') + (remainder - 1))
            columnNumber = (columnNumber - remainder) // 26
            ans = char + ans
        return ans
# @lc code=end
# print(Solution().convertToTitle(29))
