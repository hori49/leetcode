#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex+1):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                res.append([1] + [res[i-1][j] + res[i-1][j+1] for j in range(i-1)] + [1])
        return res[rowIndex]
# @lc code=end

