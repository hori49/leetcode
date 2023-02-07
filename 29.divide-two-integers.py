#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # need to handle the overflow case
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = dividend // divisor
        if sign == 1 and ans > INT_MAX:
            return INT_MAX
        elif sign == -1 and ans > INT_MAX + 1:
            return INT_MIN
        else:
            return sign * ans

# @lc code=end

