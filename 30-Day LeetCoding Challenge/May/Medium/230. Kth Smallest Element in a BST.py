"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.kthSmallest = -1
        
        def dfs(root):
            if not root:
                return False
            
            if(dfs(root.left)):
                return True
            
            if self.k == 1:
                self.kthSmallest =  root.val
                return True
            self.k -= 1
            
            if(dfs(root.right)):
                return True
            
            return False
            
        dfs(root)
        return self.kthSmallest
        