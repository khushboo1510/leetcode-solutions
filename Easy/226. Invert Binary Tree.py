"""
https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def invertChildren(root: TreeNode):
            if root:
                temp = root.left
                root.left = root.right
                root.right = temp
                invertChildren(root.left)
                invertChildren(root.right)
        
        invertChildren(root)
        
        return root