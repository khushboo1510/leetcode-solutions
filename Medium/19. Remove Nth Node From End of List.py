"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        result = ListNode(-1)
        result.next = head
        fast = slow = result
        count = 0
        d = {}
        
        while n >= 0:
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return result.next