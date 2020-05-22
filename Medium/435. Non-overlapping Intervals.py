"""
https://leetcode.com/problems/non-overlapping-intervals/

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        
        intervals.sort(key = lambda x: x[1])
        
        prev = intervals[0]
        count = 0
        
        for interval in intervals[1:]:
            if interval[0] < prev[1]:
                count += 1
                continue
            prev = interval
            
        return count