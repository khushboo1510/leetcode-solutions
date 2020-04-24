"""
https://leetcode.com/problems/diameter-of-binary-tree/submissions/

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.diameter = 0
        def depth(node: TreeNode):
            if not node:
                return 0
            
            dLeft = depth(node.left)
            dRight = depth(node.right)
            
            self.diameter = dLeft + dRight if dLeft + dRight > self.diameter else self.diameter
            
            return max(dLeft, dRight) + 1
        
        depth(root)
        
        return self.diameter