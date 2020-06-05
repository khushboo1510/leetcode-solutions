"""
https://leetcode.com/problems/random-pick-with-weight/

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
"""

class Solution:

    l = []
    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.l = w
        
    def pickIndex(self) -> int:
        num = random.randint(1, self.l[-1])
        i = 0
        j = len(self.l)
        while i < j:
            mid = (i+j) // 2
            if num == self.l[mid]:
                return mid
            elif num > self.l[mid]:
                i = mid+1
            else:
                j = mid
        return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
