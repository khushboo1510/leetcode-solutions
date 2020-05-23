"""
https://leetcode.com/problems/interval-list-intersections/

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
"""

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        result = []
        
        i = j = 0
        
        na = len(A)
        nb = len(B)
        
        while(i < na and j < nb):
            ai, aj = A[i]
            bi, bj = B[j]
            
            if ai <= bi <= aj or bi <= ai <= bj:
                result.append([max(ai, bi),  min(aj, bj)])
            
            if aj < bj:
                i += 1
            else:
                j += 1
                
        return result