#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while ((n+1)*(n+1) <= x):
            n += 1
        return n
# @lc code=end

