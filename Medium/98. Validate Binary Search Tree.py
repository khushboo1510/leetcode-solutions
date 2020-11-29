# https://leetcode.com/problems/validate-binary-search-tree/
    
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        stack = [[root, float('-inf'), float('inf')]]
        
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            if node.val <= lower or node.val >= upper:
                return False
            stack.append([node.right, node.val, upper])
            stack.append([node.left, lower, node.val])
            
        return True
