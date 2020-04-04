"""
Question:
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
"""

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        squares = []
        for x in A:
            squares.append(x**2)
        squares.sort()
        return squares