# https://leetcode.com/problems/flipping-an-image/
    
# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n, m = len(A), len(A[0])
        for row in A:
            for i in range(m // 2):
                row[i], row[m - i - 1] = row[m - i - 1], row[i]
            for i in range(m):
                row[i] = 1 if row[i] == 0 else 0
                
        return A
