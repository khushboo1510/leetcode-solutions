"""
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
    Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        result = prev = ListNode(-1)
        result.next = head
        
        while head:
            if head.next:
                node1 = head
                node2 = head.next
                node1.next = node2.next
                prev.next = node2
                node2.next = node1
                prev = head
            head = head.next
            
        return result.next