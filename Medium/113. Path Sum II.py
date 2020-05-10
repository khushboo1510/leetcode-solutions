"""
https://leetcode.com/problems/path-sum-ii/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        result = []
        
        def traverse(root, arr, total):
            
            if not root:
                return
            
            arr = arr + [root.val]
            total += root.val
            
            if not root.left and not root.right:
                if sum == total:
                    result.append(arr)
                return
                
            traverse(root.left, arr, total)
            traverse(root.right, arr, total)    
                
        traverse(root,[],0)
        return result