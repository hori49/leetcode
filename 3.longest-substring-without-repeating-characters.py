#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        lst = []
        ans = 0
        tmp = 0
        i = 0
        while (i < N):
            if s[i] in lst:
                ans = max(ans, tmp)
                i = i-tmp+1
                tmp = 0
                lst = []
            else:
                lst.append(s[i])
                tmp += 1
                i += 1
        return max(ans, tmp)
# @lc code=end

