"""
https://leetcode.com/problems/sort-array-by-parity/

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        odd = []
        even = []
        
        for a in A:
            if a % 2 != 0:
                odd.append(a)
            else:
                even.insert(0,a)
        return even + odd