"""
https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
    Input:
        [
          1->4->5,
          1->3->4,
          2->6
        ]
    Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        heap = []
        n = 0
        for i, LL in enumerate(lists):
            if LL:
                heapq.heappush(heap, (LL.val, i, LL))
                n += 1

        result = head = ListNode(-1)
        while heap:
            val, i, node = heapq.heappop(heap)
            if n > 1:
                head.next= node
                head = head.next

                if node.next:
                    heapq.heappush(heap, (node.next.val, i, node.next))
                else:
                    n -= 1
            else:
                head.next = node
                break
        return result.next