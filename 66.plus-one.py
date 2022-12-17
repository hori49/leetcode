#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits):
        N = len(digits)
        num = 0
        for i in range(N):
            num += digits[i] * 10**(N-1-i)
        num += 1

        lst = []
        while (num > 0):
            lst.append(num % 10)
            num = num // 10
        lst.reverse()

        return lst
# @lc code=end

