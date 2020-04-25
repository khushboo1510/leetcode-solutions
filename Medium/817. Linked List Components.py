"""
https://leetcode.com/problems/linked-list-components/

We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        g = set(G)
        count = 0
        
        while head:
            if head.val in g:
                count += 1
                while head and head.val in g:
                    head = head.next
            else:
                head = head.next
        
        return count