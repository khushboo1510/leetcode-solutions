# https://leetcode.com/problems/permutation-sequence/

# The set [1,2,3,...,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

#     1. "123"
#     2. "132"
#     3. "213"
#     4. "231"
#     5. "312"
#     6. "321"
# Given n and k, return the kth permutation sequence.

# Note:
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        lst = [str(i) for i in range(1,n + 1)]
        result = ""
        while lst:
            divisor = factorial(n - 1)
            quo = floor(k / divisor)
            if k % divisor == 0:
                quo -= 1
            k %= divisor
            result += lst.pop(quo)
            n -= 1
    
        return result