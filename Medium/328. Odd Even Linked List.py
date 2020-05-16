"""
https://leetcode.com/problems/odd-even-linked-list/

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        oddLL = head
        evenLL = head2 = head.next
        
        while evenLL and evenLL.next:
            
            oddLL.next = oddLL.next.next
            oddLL = oddLL.next
            evenLL.next = evenLL.next.next
            evenLL = evenLL.next
                
                
        oddLL.next = head2        
        return head