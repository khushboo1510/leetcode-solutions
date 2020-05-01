"""
https://leetcode.com/problems/binary-tree-tilt/

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        self.total = 0
        
        def dfs(root):
            
            if not root.left and not root.right:
                return root.val
            
            leftsum = rightsum = 0
            
            if root.left:
                leftsum = dfs(root.left)
            if root.right:
                rightsum = dfs(root.right)
                
            self.total += abs(rightsum - leftsum)
            
            return rightsum + leftsum + root.val
        
        dfs(root)
        return self.total