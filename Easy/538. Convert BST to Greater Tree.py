"""
https://leetcode.com/problems/convert-bst-to-greater-tree/

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        def dfs(root, total):
            
            if not root:
                return total
            
            root.val += dfs(root.right, total)
            return dfs(root.left, root.val)
        
        dfs(root, 0)
        return root