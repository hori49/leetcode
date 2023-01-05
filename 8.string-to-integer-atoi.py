#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        N = len(s)
        idx = 0
        while(idx < N and s[idx] == ' '):
            idx += 1
        if (idx == N):
            return 0
        else:
            if (s[idx] == '-'):
                sign = -1
                idx += 1
            elif (s[idx] == '+'):
                sign = 1
                idx += 1
            else:
                sign = 1

            num = 0
            while(idx < N and s[idx] >= '0' and s[idx] <= '9'):
                num = num * 10 + int(s[idx])
                idx += 1
            num = sign * num

            if (num < -2**31):
                return -2**31
            elif (num > 2**31-1):
                return 2**31-1
            else:
                return num
# @lc code=end

# def main():
#     s = "  42"
#     i = Solution.myAtoi(Solution, s)
#     print(i)

# if __name__ == "__main__":
#     main()
