"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.maxValue = -pow(2,31)
        
        def findMax(root):
            if not root:
                return -pow(2,31)

            left = findMax(root.left)
            right = findMax(root.right)

            total = root.val + left + right
            
            if self.maxValue < max(total, left, right):
                self.maxValue = max(total, left, right)

            return max(root.val, root.val + left, root.val + right)
        
        return max(findMax(root), self.maxValue)