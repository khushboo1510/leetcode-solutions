"""
https://leetcode.com/problems/univalued-binary-tree/

A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        s = set()
        
        def traverse(root) -> bool:
            if root:
                s.add(root.val)
                traverse(root.left)
                traverse(root.right)
        
        traverse(root)
        
        return len(s) == 1   