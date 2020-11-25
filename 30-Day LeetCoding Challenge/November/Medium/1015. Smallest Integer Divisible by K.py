# https://leetcode.com/problems/smallest-integer-divisible-by-k/solution/
    
# Given a positive integer K, you need to find the length of the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

# Return the length of N. If there is no such N, return -1.

# Note: N may not fit in a 64-bit signed integer.
    
# Constraints:
#     1 <= K <= 105

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        remainders = set()
        N = l = 1
        while 1:
            r = N % K
            if r == 0:
                return l
            if r in remainders:
                return -1
            l += 1
            remainders.add(r)
            N = N * 10 + 1
        return -1
