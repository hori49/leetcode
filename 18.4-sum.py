#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

from typing import List
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        ans = []
        nums.sort()
        for i in range (N-3):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            for j in range (i+1, N-2):
                if (j > i+1 and nums[j] == nums[j-1]):
                    continue
                k = j + 1
                l = N - 1
                while (k < l):
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if (sum == target):
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        while (k < l and nums[k] == nums[k+1]):
                            k += 1
                        while (k < l and nums[l] == nums[l-1]):
                            l -= 1
                        k += 1
                        l -= 1
                    elif (sum < target):
                        k += 1
                    else:
                        l -= 1
        return ans
# @lc code=end

