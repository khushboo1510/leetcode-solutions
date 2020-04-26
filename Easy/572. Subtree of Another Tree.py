"""
https://leetcode.com/problems/subtree-of-another-tree/submissions/

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def check(s: TreeNode, t: TreeNode):
            if not s and not t:
                return True
        
            if not s or not t:
                return False
        
            if s.val == t.val:
                return check(s.left, t.left) and check(s.right, t.right)
            return False
        
        if not s and not t:
            return True
        
        if not s or not t:
            return False

        return check(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            
        