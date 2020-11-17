# https://leetcode.com/problems/longest-mountain-in-array/
    
# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)

# Given an array A of integers, return the length of the longest mountain. 

# Return 0 if there is no mountain.

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        max_count = start = end = 0
        n = len(A)
        up = True
        for i in range(len(A)):
            if up:
                if A[i - 1] == A[i]:
                    start = i
                elif A[i - 1] > A[i]:
                    if start != end:
                        up = False
                    else:
                        start = i
                end = i
            else:
                if A[i - 1] <= A[i]:
                    if end - start + 1 >= 3:
                        max_count = max(max_count, end - start + 1)
                    if A[i - 1] == A[i]:
                        start = i
                    else:
                        start = end
                    up = True
                end = i
    
        if not up and end - start + 1 >= 3:
            max_count = max(max_count, end - start + 1)
        return max_count
