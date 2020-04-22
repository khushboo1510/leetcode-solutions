# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        temp = ListNode(0)
        result = temp
        quotient = 0
        
        while l1 or l2 or quotient == 1:
            x, y = 0, 0
            
            if l1:
                x = l1.val
                l1 = l1.next
            if l2:
                y = l2.val
                l2 = l2.next
                
            num = x + y + quotient
            temp.next = ListNode(num % 10)
            temp = temp.next
            quotient = num // 10
        
            
        return result.next