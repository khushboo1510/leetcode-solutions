"""
https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        def dfs(left,right):
            
            if left and right:
                if left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left):
                    return True
            return left == right
        
        return dfs(root.left, root.right)