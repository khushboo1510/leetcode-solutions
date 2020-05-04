"""
https://leetcode.com/problems/partition-list/submissions/

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:
    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        if not head:
            return head
        
        result = prev = wait = ListNode(-1)
        result.next = head
        while head:
            if head.val >= x:
                prev = head
                head = head.next
                continue
                
            if head.val < x and prev == wait:
                prev = prev.next
                wait = prev
                head = head.next
                continue
            temp2 = wait.next
            wait.next = head
            prev.next = head.next
            head.next = temp2
            head = prev.next
            wait = wait.next
        return result.next