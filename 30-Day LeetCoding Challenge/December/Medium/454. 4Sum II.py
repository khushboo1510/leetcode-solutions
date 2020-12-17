# https://leetcode.com/problems/4sum-ii/
    
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if not A:
            return 0
        
        CntAB, CntCD = defaultdict(int), defaultdict(int)
        
        for a, b in product(A, B):
            CntAB[a + b] += 1
            
        for c, d in product(C, D):
            CntCD[c + d] += 1
                
        count = 0
        
        for key, value in CntAB.items():
            if CntCD[-key]:
                count += value * CntCD[-key]   
                
        return count
