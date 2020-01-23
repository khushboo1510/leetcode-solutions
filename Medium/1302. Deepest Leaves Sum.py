# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.d = collections.defaultdict(int)

        def dfs(root, counter):
            if root is None:
                return
            self.d[counter] += root.val

            dfs(root.left, counter + 1)
            dfs(root.right, counter + 1)

        dfs(root, 0)
        return max(self.d.items(), key=operator.itemgetter(0))[1]
