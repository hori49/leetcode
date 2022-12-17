#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        N = len(nums)
        k = 0
        lst = []
        for i in range(N):
            if nums[i] not in lst:
                lst.append(nums[i])
            else:
                k += 1

        for i in range (N-k):
            nums[i] = lst[i]
        return N - k
# @lc code=end

