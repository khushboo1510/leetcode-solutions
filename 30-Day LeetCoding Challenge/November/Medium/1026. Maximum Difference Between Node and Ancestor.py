# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
    
# Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

# A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.result = 0
        
        def dfs(node):
            if not node:
                return sys.maxsize, -sys.maxsize
            
            if not node.right and not node.left:
                return node.val, node.val
            
            minL, maxL = dfs(node.left)
            minR, maxR = dfs(node.right)
            minN, maxN = min(minL, minR), max(maxL, maxR)
            self.result = max(self.result, abs(minN - node.val), abs(maxN - node.val))
            
            return min(minN, node.val), max(maxN, node.val)
        
        dfs(root)
        return self.result
