"""
https://leetcode.com/problems/same-tree/

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
       
        def traverse(root: TreeNode):
            
            result = []
            
            if not root:
                return [-1]
            else:
                result.append(root.val)
                result.extend(traverse(root.left))
                result.extend(traverse(root.right))
                return result
        return traverse(p) == traverse(q)