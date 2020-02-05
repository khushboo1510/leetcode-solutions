# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 1
        while(queue):
            new_level = []
            for node in queue:
                if not node.right and not node.left:
                    return depth
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            queue = new_level
            
            depth += 1
        return depth
        