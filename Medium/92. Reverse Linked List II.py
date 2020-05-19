"""
https://leetcode.com/problems/reverse-linked-list-ii/

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if m == n:
            return head
        i = 0
        prev, start, end = None, None, None
        result = ListNode(-1, head)
        result.next, head = head, result

        for i in range(m):
            start = head
            head = head.next
        i = m
        while(i <= n):
            
            curr, head = head, head.next
            curr.next = prev
            prev = curr
            i += 1
            end = head
             
        start.next.next = end
        start.next = prev
        return result.next