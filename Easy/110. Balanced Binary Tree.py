"""
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        self.flag = True
        
        def checkHeight(root):
            
            if not self.flag:
                return 0
            
            if not root:
                return 0
            
            hleft = checkHeight(root.left)
            hright = checkHeight(root.right)
            
            if abs(hleft - hright) > 1:
                self.flag = False
                return 0
            
            return max(hleft, hright) + 1
        
        checkHeight(root)
        
        return self.flag