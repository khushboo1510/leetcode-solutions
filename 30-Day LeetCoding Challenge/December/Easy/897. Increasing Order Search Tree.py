# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return
        root.right = self.increasingBST(root.right)
        root.left = self.increasingBST(root.left)
        temp = root
        if root.left:
            temp = root.left
            root.left = None
            node = temp
            while node.right:
                node = node.right
            node.right = root
        return temp
