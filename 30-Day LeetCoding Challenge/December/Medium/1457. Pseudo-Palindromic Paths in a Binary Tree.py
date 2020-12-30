# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        l = [0 for _ in range(10)]
        
        def dfs(l, root):
            
            if not root:
                return 0
            
            l[root.val] += 1
            
            if not root.left and not root.right:
                count = 0
                for i in range(10):
                    count += l[i] % 2
                    if count > 1:
                        return 0
                return 1
            
            return dfs(l[:], root.left) + dfs(l[:], root.right)
        
        return dfs(l, root)
