# https://leetcode.com/problems/trapping-rain-water/
    
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        
        mIndex, maxlevel = 0, 0
        total = 0
        n = 0
        
        for i, x in enumerate(height):
            if x > maxlevel:
                maxlevel = x
                mIndex = i
            n += 1

        maxLeft = 0
        for i in range(1, mIndex):
            maxLeft = max(maxLeft, height[i - 1])
            if maxLeft > height[i]:
                total += (maxLeft - height[i])

        maxRight = 0
        for i in range(n - 2, mIndex, -1):
            maxRight = max(maxRight, height[i + 1])
            if height[i] < maxRight:
                total += (maxRight - height[i])
                
        return total