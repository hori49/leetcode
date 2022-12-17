#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums, target) -> int:
        N = len(nums)
        k = 0
        for i in range(N):
            if (nums[i] < target):
                k += 1
            else:
                return k
        return k
# @lc code=end

