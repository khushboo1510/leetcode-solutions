# https://leetcode.com/problems/sum-root-to-leaf-numbers/
    
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        self.sum = 0
        
        def dfs(root, num):
            if not root:
                return
            num += root.val
            if not root.left and not root.right:
                self.sum += num  
                return
            num *= 10
            dfs(root.left, num)
            dfs(root.right, num)
            
        dfs(root, 0)
        return self.sum