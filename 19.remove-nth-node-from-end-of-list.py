#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

from typing import Optional
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        behind = ahead = head
        for _ in range(n):
            ahead = ahead.next
        if ahead is None:
            head = head.next
            return head
        while ahead.next is not None:
            ahead = ahead.next
            behind = behind.next
        curr = behind.next
        behind.next = curr.next
        return head
# @lc code=end

