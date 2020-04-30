"""
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Problem is similar to concept of Trie
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        
        #return false if tree or arr exists and the other one doesn't
        if not root or not arr:
            return False
        
        #if true then DFS
        if root.val == arr[0]:
           
            #if array becomes empty once the value has been checked, check if the current node is a leaf node
            if not arr[1:]:
                
                #if leaf node, return true
                if not root.left and not root.right:
                    return True
                #else false because arr becomes empty but the node still have children
                return False
            
            #if arr is not empty, then DFS for the remaining elements in arr
            return self.isValidSequence(root.left, arr[1:]) or self.isValidSequence(root.right, arr[1:])