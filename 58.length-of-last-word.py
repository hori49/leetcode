#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = []
        for i in range (len(s)):
            lst.append(s[i])
        N = len(lst)
        lst.append(' ')
        str_len = 0
        for i in range (N):
            if (lst[i] != ' '):
                str_len += 1
            else: # s[N-1-i] == ' '
                if (lst[i+1] == ' '):
                    continue
                else:
                    str_len = 0
        return str_len
# @lc code=end

# def main():
#     s = "For debugging purpose  "
#     # Run the solution class
#     ret = Solution.lengthOfLastWord(Solution, s)
#     print("Ans =", ret)

# if __name__ == '__main__':
#     main()
