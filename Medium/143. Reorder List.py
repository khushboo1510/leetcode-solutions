"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow = fast = pt = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        reverse = None

        while slow:
            curr = slow
            slow = slow.next
            curr.next = reverse
            reverse = curr

        while reverse.next:
            new = reverse
            reverse = reverse.next
            curr = pt.next
            new.next = curr
            pt.next = new
            pt = curr
