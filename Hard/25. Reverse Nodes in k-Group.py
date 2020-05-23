"""
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
    Given this linked list: 1->2->3->4->5
    For k = 2, you should return: 2->1->4->3->5
    For k = 3, you should return: 3->2->1->4->5

Note:
    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
       
        if not head or k == 1:
            return head
        node = head
        
        for _ in range(k - 1):
            node = node.next
            if not node:
                return head
            
        cur = head
        prev, end = None, cur
        count = 1
        
        while(count <= k):
            temp = cur
            cur, temp.next = cur.next, prev
            prev = temp
            count += 1
        
        end.next = self.reverseKGroup(cur, k)
        
        return prev