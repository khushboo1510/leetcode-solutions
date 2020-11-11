# https://leetcode.com/problems/valid-square/
    
# Given the coordinates of four points in 2D space, return whether the four points could construct a square.

# The coordinate (x,y) of a point is represented by an integer array with two integers.

# Note:

# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def euclideanDistance(x, y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
        
        distances = defaultdict(int)
        distances[euclideanDistance(p1,p2)] += 1
        distances[euclideanDistance(p2,p3)] += 1
        distances[euclideanDistance(p3,p4)] += 1
        distances[euclideanDistance(p4,p1)] += 1
        distances[euclideanDistance(p2,p4)] += 1
        distances[euclideanDistance(p3,p1)] += 1
        
        return len(distances) == 2 and 2 in distances.values() and 4 in distances.values() 
