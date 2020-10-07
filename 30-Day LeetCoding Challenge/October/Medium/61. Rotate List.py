# https://leetcode.com/problems/rotate-list/
    
# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        n = 0
        temp = last = head 
        while temp:
            n += 1
            last, temp = temp, temp.next
            
        k = k % n
        if k == 0:
            return head
        
        k = n - k
        curr = prev = head
        while k:
            prev, curr = curr, curr.next
            k -= 1
            
        last.next, prev.next = head, None
        return curr
