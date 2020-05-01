# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
https://leetcode.com/problems/cousins-in-binary-tree/

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
"""

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        k = 0
        queue = [root]
        d = {}
        d[root.val] = [0, None]
        
        while queue:
            node = queue.pop(0)
            k, parent = d.get(node.val)
            if node.left:
                queue.append(node.left)
                d[node.left.val] = [k + 1, node]
            if node.right:
                queue.append(node.right)
                d[node.right.val] = [k + 1, node]
        
        kx, parentx = d.get(x)
        ky, parenty = d.get(y)
        
        if kx == ky and parentx != parenty:
            return True
        return False