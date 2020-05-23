"""
https://leetcode.com/problems/remove-covered-intervals/

Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.
"""

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], -x[1]))
        
        count = len(intervals)
        
        px, py = intervals[0]
        
        for x, y in intervals[1:]:
            if px <= x and y <= py:
                count -= 1
            else:
                px, py = x, y

        return count