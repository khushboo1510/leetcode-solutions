# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
    
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that A[i] and B[i] swap values.

# Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

# If it cannot be done, return -1.

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        count_a, count_b, count_same = defaultdict(int), defaultdict(int), defaultdict(int)
        
        for a, b in zip(A, B):
            count_a[a] += 1
            count_b[b] += 1
            if a == b:
                count_same[a] += 1
                if len(count_same) > 1:
                    return -1
                
        if count_same:
            for key, value in count_same.items():
                if n - value == count_a[key] + count_b[key] - (value * 2):
                    return min(count_a[key], count_b[key]) - value
        else:
            rotations, flag = sys.maxsize, False
            for key, value in count_a.items():
                if value + count_b[key] == n:
                    rotations, flag = min(rotations, count_a[key], count_b[key]), True
            if flag:
                return rotations
        return -1
