# https://leetcode.com/problems/serialize-and-deserialize-bst/
    
# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import pickle
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return '#'
        return str(root.val) + '-' + self.serialize(root.left) + '-' + self.serialize(root.right)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = data.split('-')
        self.count = 0
        
        def traverse():
            if data[self.count] == '#':
                self.count += 1
                return None
            root = TreeNode(int(data[self.count]))
            self.count += 1
            root.left = traverse()
            root.right = traverse()
            return root
        return traverse()
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
