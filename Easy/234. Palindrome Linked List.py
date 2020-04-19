"""
Given a singly linked list, determine if it is a palindrome.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        
        slow = fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            curr = ListNode(slow.val)
            slow = slow.next
            curr.next = prev
            prev = curr

        while prev is not None:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
        return True
    