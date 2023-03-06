#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low, high = prices[0], prices[0]
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
                high = prices[i]
            elif prices[i] > high:
                high = prices[i]
                profit = max(profit, high - low)
        return profit
# @lc code=end

