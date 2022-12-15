#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        lst = []
        lst.append(target - nums[0])
        for i in range (1, n):
            if (nums[i] in lst):
                return lst.index(nums[i]), i
            else:
                lst.append(target - nums[i])
# @lc code=end

