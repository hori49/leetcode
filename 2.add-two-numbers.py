#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (l1 is None and l2 is None):
            return None
        elif (l1 is None):
            return l2
        elif (l2 is None):
            return l1
        elif (l1.val + l2.val < 10):
            return ListNode(l1.val + l2.val, self.addTwoNumbers(l1.next, l2.next))
        else:
            return ListNode(l1.val + l2.val - 10, self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next)))
# @lc code=end

