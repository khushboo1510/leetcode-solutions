# https://leetcode.com/problems/the-kth-factor-of-n/
    
# Given two positive integers n and k.

# A factor of an integer n is defined as an integer i where n % i == 0.

# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        for i in range(1, 1 + n // 2):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        if k == 1:
            return n
        return -1
