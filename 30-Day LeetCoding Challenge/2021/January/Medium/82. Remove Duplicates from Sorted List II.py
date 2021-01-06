# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
    
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        result = prev = ListNode(0, head)
        while head and head.next:
            if head.val == head.next.val:
                dup = head.val
                while head and dup == head.val:
                    head = head.next
                prev.next = head
            else:
                prev = head
                head = head.next
            
        return result.next
