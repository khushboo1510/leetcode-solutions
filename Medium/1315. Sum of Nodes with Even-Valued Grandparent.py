# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        self.sum = 0

        def getNext(r):
            if r is None:
                return

            if r.val % 2 == 0:
                if r.left is not None:
                    if r.left.left is not None:
                        self.sum += r.left.left.val
                    if r.left.right is not None:
                        self.sum += r.left.right.val
                if r.right is not None:
                    if r.right.left is not None:
                        self.sum += r.right.left.val
                    if r.right.right is not None:
                        self.sum += r.right.right.val

            getNext(r.left)
            getNext(r.right)

        getNext(root)
        return self.sum