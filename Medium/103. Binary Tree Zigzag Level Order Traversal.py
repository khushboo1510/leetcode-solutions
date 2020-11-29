# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = defaultdict(list)
        if not root:
            return []
        queue = deque()
        queue.append([root, 0])
        while queue:
            node, level = queue.popleft()
            if node:
                result[level].append(node.val)
                queue += [[node.left, level + 1], [node.right, level + 1]]
        
        return result.values()
