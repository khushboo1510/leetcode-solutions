"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
"""

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        
        while stones:
            heapq._heapify_max(stones)
            if len(stones) == 1:
                return heapq._heappop_max(stones)
            
            heapq.heappush(stones, heapq._heappop_max(stones) - heapq._heappop_max(stones))
        
        return 0
        