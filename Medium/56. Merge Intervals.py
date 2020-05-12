"""
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example:
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        
        intervals.sort(key = lambda x: x[0])
        stack = [intervals[0]]
        for interval in intervals[1:]:
            x = stack.pop()
            if x[1] >= interval[0]:
                x[1] = max(x[1], interval[1])
                stack.append(x)
            else:
                stack.append(x)
                stack.append(interval)
            
        return stack