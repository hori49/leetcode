#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        else:
            s = str(x)
            n = len(s)
            for i in range (int(n/2)):
                if (s[i] == s[n-i-1]):
                    continue
                else:
                    return False
        return True
# @lc code=end

