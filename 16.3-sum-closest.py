#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range (N-2):
            j = i + 1
            k = N - 1
            while (j < k):
                sum = nums[i] + nums[j] + nums[k]
                if (sum == target):
                    return sum
                if (abs(sum-target) < abs(ans-target)):
                    ans = sum
                if (sum < target):
                    j += 1
                else:
                    k -= 1
        return ans
# @lc code=end

