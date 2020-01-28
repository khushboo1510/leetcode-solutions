# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        queue = [root]
        totol = 0
        
        while queue:
            new_level = []
            total = 0
            for node in queue:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
                total += node.val
            
            queue = new_level
            
        return total
            
    