#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        for i in nums:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        sorted_mp = sorted(mp.items(), key=lambda x: x[1], reverse=True)
        return sorted_mp[0][0]
# @lc code=end
# print(Solution().majorityElement([2,2,1,1,1,2,2]))
