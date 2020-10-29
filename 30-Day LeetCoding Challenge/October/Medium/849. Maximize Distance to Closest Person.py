# https://leetcode.com/problems/maximize-distance-to-closest-person/
    
# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

# Return that maximum distance to the closest person.

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxx, start, n = 0, -1, len(seats)
        
        for i in range(n):
            if seats[i] == 1:
                if start == -1:
                    maxx = i
                else:
                    maxx = max((i - start) // 2, maxx)
                start = i
        maxx = max(n - 1 - start, maxx)
        return maxx
