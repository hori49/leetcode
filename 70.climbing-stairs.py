#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        lst = []
        lst.append(0)
        lst.append(1)
        lst.append(2)
        for i in range(3, n+1):
            lst.append(lst[i-1] + lst[i-2])
        return lst[n]
# @lc code=end

