# https://leetcode.com/problems/range-sum-of-bst/
    
# Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total = 0
        if root:
            if low <= root.val <= high:
                total += root.val
            if root.val <= high:
                total += self.rangeSumBST(root.right, low, high)
            if low <= root.val:
                total += self.rangeSumBST(root.left, low, high)
        return total
