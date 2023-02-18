#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return

        # Find the pivot
        pivot = len(nums) - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot+1]:
            pivot -= 1

        # If there is a pivot, find the smallest element to the right of
        # the pivot that is greater than the pivot
        if pivot >= 0:
            successor = len(nums) - 1
            while successor >= 0 and nums[successor] <= nums[pivot]:
                successor -= 1
            nums[pivot], nums[successor] = nums[successor], nums[pivot]

        # Reverse the elements to the right of the pivot
        left, right = pivot+1, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
# @lc code=end

