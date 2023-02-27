#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Count the number of occurrences of each element
        counts = Counter(nums)
        # Find the element with only one occurrence
        for num, count in counts.items():
            if count == 1:
                return num

# @lc code=end

