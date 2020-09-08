# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
    
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

# Return the sum of these numbers.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        self.total = 0
        
        def dfs(s: str, root: TreeNode):
            
            if not root:
                return
            
            ch = str(root.val)
            
            if not root.left and not root.right:
                self.total += int(s + ch, 2) 
                return
            
            dfs(s + ch, root.left)
            dfs(s + ch, root.right)
            
        dfs('', root)
        
        return self.total