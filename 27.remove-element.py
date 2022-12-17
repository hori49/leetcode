#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums, val) -> int:
        N = len(nums)
        k = 0
        lst = []
        for i in range(N):
            if (nums[i] != val):
                lst.append(nums[i])
            else:
                k += 1

        for i in range (N-k):
            nums[i] = lst[i]
        return N - k

# @lc code=end

