#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        st = str(x)
        if (st[0] == '-'):
            st = st[0] + st[1:][::-1]
        else:
            st = st[::-1]
        ans = int(st)
        return ans if ans.bit_length() < 32 else 0
# @lc code=end

