# https://leetcode.com/problems/h-index-ii/
    
# Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if not citations or citations[-1] == 0:
            return 0
        
        n = len(citations)
        
        if n == 1 and citations[0] == 0:
            return 0
        
        left, right = 0, n
        res = 0
        while left <= right:
            mid = (left+right)//2
            if n - mid >= citations[mid]:
                if n - mid == citations[mid]:
                    return citations[mid]
                else:
                    res = max(res, mid)
                    left = mid + 1
            else:
                right = mid - 1
        if citations[res] >= n:
            return n - res
        return n - left