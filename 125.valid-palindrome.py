#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a new string with only alphanumeric characters
        new_s = [char.lower() for char in s if char.isalnum()]

        # Check if the string is a palindrome
        left, right = 0, len(new_s) - 1
        while (left < right):
            if (new_s[left] != new_s[right]):
                return False
            left += 1
            right -= 1
        return True

# @lc code=end

