# https://leetcode.com/problems/unique-binary-search-trees/
    
# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

class Solution:
    def numTrees(self, n: int) -> int:
        
        self.d = {1:1,0:0}

        def bst(n):
            if n in self.d:
                return self.d[n]
            else:
                i, result = 0, 0
                while i < n:
                    ln, rn = i, n - 1 - i
                    left, right = bst(ln), bst(rn)
                    self.d[ln] = left
                    self.d[rn] = right
                    if left != 0 and right != 0:
                        result += left * right
                    else:
                        result += left + right
                    i += 1
                return result
            
        return bst(n)