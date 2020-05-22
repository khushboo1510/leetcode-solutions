"""
https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        stack = []
        start, end = newInterval
        k = 0
        for i, j in intervals:
            if start <= j:
                if end < i:
                    break
                start = min(i, start)
                end = max(j, end)
            else:
                stack.append([i, j])
            k += 1
            
        stack.append([start, end])
        stack += intervals[k:]
        
        return stack