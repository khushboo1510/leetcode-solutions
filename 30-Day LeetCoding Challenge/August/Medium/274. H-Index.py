# https://leetcode.com/problems/h-index/
    
# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
    

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h = 0
        
        for i in range(n):
            if citations[i] >= len(citations[i:]):
                h = max(h, len(citations[i:]))
                
        return h