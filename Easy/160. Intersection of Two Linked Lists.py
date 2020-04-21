"""
Write a program to find the node at which the intersection of two singly linked lists begins.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

Method 1: Two while loops to match the heads O(n^2)
Method 2: use 2 hashmap to store pointer to each node for Linkedlist A & B and check the incoming node in the other hashmap i.e. check node from LL-A in hashmap of B.  O(n) time and additional memory for hashmap
Method 3: iterate both the LL in one loop and calculate the difference in length. start the longer LL from the difference value.  O(n) time and O(1) memory

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        currA = headA
        currB = headB
        while currA and currB:
            currA = currA.next
            currB = currB.next
        
        counter = short = long = None
        if currA:
            counter = currA
            short, long = headB, headA
        else:
            counter = currB
            short, long = headA, headB
            
        while counter:
            long = long.next
            counter = counter.next
            
        while long and short:
            if long == short:
                return long
            long = long.next
            short = short.next
        
        return None
            
            