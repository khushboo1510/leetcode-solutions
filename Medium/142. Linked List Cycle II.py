"""
https://leetcode.com/problems/linked-list-cycle-ii/

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Follow-up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        slow = fast = head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                flag = True
                break
        if flag:      
            slow = head
            while slow:
                if slow == fast:
                    return slow
                slow, fast = slow.next, fast.next
