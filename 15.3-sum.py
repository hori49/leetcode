#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        nums.sort()
        for i in range (N-2):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            j = i + 1
            k = N - 1
            while (j < k):
                sum = nums[i] + nums[j] + nums[k]
                if (sum == 0):
                    ans.append([nums[i], nums[j], nums[k]])
                    while (j < k and nums[j] == nums[j+1]):
                        j += 1
                    while (j < k and nums[k] == nums[k-1]):
                        k -= 1
                    j += 1
                    k -= 1
                elif (sum < 0):
                    j += 1
                else:
                    k -= 1
        return ans
# @lc code=end

