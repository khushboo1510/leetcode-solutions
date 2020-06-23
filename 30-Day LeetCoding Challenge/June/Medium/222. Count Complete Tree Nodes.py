# https://leetcode.com/problems/count-complete-tree-nodes/
    
# Given a complete binary tree, count the number of nodes.

# Note:

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        leftD = 1 + self.getDepth(root.left, True)
        rightD = 1 + self.getDepth(root.right, False)
        
        if leftD == rightD:
            return 2 ** leftD - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    def getDepth(self, node, isLeft):
        if not node:
            return 0
        
        if isLeft:
            return 1 + self.getDepth(node.left, True)
        else:
            return 1 + self.getDepth(node.right, False)