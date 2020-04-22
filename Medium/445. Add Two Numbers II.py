"""
https://leetcode.com/problems/add-two-numbers-ii/

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

Method1: iterate both LL and store values in stack. Pop them while adding the number and storing it to new LL
Method2: iterate both LL and generate num = num*10 + ll.val. Add those numbers, convert result to list and add elements of list to string.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def reverse(ll: ListNode):
            res = None
            while ll:
                tem = ll
                ll = ll.next
                tem.next = res
                res = tem
            return res
        
        l1 = reverse(l1)
        l2 = reverse(l2)

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
        
            
        return reverse(result.next)