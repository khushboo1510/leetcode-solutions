# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
    
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.
# Follow up:

# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        curr, leftmost = root, root.left
        
        while curr and curr.left:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
                curr = curr.next
            else:
                curr = leftmost
                leftmost = curr.left
            
        return root
       
"""
# Another Solution
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = [[root, 0]]
        
        while queue:
            node, level = queue.pop(0)
            
            if queue and queue[0][1] == level:
                node.next = queue[0][0]
            if node and node.left:
                queue.append([node.left, level + 1])
                queue.append([node.right, level + 1])
        return root
"""
        
