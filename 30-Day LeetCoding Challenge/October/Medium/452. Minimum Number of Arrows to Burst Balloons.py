# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
    
# There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.

# An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.

# Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: (x[0],x[1]))
        x1, x2 = points.pop(0)
        count = 1
        while points:
            p1, p2 = points.pop(0)
            if p1 <= x2:
                x1, x2 = p1, min(p2, x2)
            else:
                x1, x2 = p1, p2
                count += 1
        return count
