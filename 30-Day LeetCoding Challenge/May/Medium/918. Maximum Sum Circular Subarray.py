"""
https://leetcode.com/problems/maximum-sum-circular-subarray/

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
"""
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:

        max_so_far, min_so_far, max_sum, min_sum, total_sum = A[0],A[0],A[0],A[0], sum(A)
        for i in range(1, len(A)):
            max_so_far = max(max_so_far+A[i],A[i])
            max_sum = max(max_sum,max_so_far)
            min_so_far = min(min_so_far+A[i],A[i])
            min_sum = min(min_sum,min_so_far)
        if min_sum==total_sum:
            return max_sum
        return max(total_sum-min_sum, max_sum)