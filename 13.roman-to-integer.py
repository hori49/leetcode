#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, st: str) -> int:
        ret = 0
        n = len(st)
        s = []
        for i in range (n):
            s.append(st[i])
        s.append('E')

        i = 0
        while (i < n):
            if (s[i] == 'I' and s[i+1] == 'V'):
                ret += 4
                i += 2
            elif (s[i] == 'I' and s[i+1] == 'X'):
                ret += 9
                i += 2
            elif (s[i] == 'X' and s[i+1] == 'L'):
                ret += 40
                i += 2
            elif (s[i] == 'X' and s[i+1] == 'C'):
                ret += 90
                i += 2
            elif (s[i] == 'C' and s[i+1] == 'D'):
                ret += 400
                i += 2
            elif (s[i] == 'C' and s[i+1] == 'M'):
                ret += 900
                i += 2
            elif (s[i] == 'I'):
                ret += 1
                i += 1
            elif (s[i] == 'V'):
                ret += 5
                i += 1
            elif (s[i] == 'X'):
                ret += 10
                i += 1
            elif (s[i] == 'L'):
                ret += 50
                i += 1
            elif (s[i] == 'C'):
                ret += 100
                i += 1
            elif (s[i] == 'D'):
                ret += 500
                i += 1
            elif (s[i] == 'M'):
                ret += 1000
                i += 1

        return ret
# @lc code=end

