"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        result = head
        
        while head and head.next:
            
            if head.next.val == head.val:
                if head.next.next:
                    head.next = head.next.next
                else:
                    head.next = None
                continue
            head = head.next
        
        return result