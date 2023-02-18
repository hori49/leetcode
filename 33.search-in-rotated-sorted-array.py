#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while (left <= right):
            mid = (left + right) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < nums[right]):
                if (target > nums[mid] and target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if (target >= nums[left] and target < nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
# @lc code=end

