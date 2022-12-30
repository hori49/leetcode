#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        # Find the longest palindrome with center at i
        N = len(s)
        for i in range(N):
            # Odd length
            j = 0
            while (i-j >= 0 and i+j < N and s[i-j] == s[i+j]):
                j += 1
            if (2*j-1 > len(ans)):
                ans = s[i-j+1:i+j]
            # Even length
            j = 0
            while (i-j >= 0 and i+1+j < N and s[i-j] == s[i+1+j]):
                j += 1
            if (2*j > len(ans)):
                ans = s[i-j+1:i+1+j]
        return ans
# @lc code=end

