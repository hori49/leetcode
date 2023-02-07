#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1
        for i in range (len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                ans = i
                break
        return ans
# @lc code=end

