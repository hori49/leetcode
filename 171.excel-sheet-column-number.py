#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        ans = 0
        for i, char in enumerate(columnTitle[::-1]):
            ans += (26 ** i) * alpha.index(char)

        return ans

# sample test case:
# s = 'AA'
# print(Solution().titleToNumber(s))
# @lc code=end

