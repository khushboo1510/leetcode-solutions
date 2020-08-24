# https://leetcode.com/problems/sum-of-left-leaves/
    
# Find the sum of all left leaves in a given binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def traverseTree(root, child):
            if not root:
                return 0
            if not root.left and not root.right:
                if child == 'L':
                    return root.val
                return 0
            return traverseTree(root.left, 'L') + traverseTree(root.right, 'R')
        
        return traverseTree(root, 'R')