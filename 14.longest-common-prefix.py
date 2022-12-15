#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res = ''
        prefix = strs[0]
        for string in strs[1:]:
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:len(prefix)-1]
            if not prefix:
                break
        res = prefix

        return res
# @lc code=end

