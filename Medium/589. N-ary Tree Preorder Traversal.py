"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/

Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return
        
        nodes = [root]
        result = []
        
        while nodes:
            node = nodes.pop(0)
            result.append(node.val)
            if node.children:
                nodes = node.children + nodes
                
        return result