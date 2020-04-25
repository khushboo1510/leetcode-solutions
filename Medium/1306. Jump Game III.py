"""
https://leetcode.com/problems/jump-game-iii/

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

EXAMPLE:
    Input: arr = [4,2,3,0,3,1,2], start = 5
    Output: true
    Explanation: 
    All possible ways to reach at index 3 with value 0 are: 
    index 5 -> index 4 -> index 1 -> index 3 
    index 5 -> index 6 -> index 4 -> index 1 -> index 3 
"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visited = []
        n = len(arr)
        
        def dfs(start: int):
            
            if start < 0 or start >= n:
                return False
            
            if start in visited:
                return False
            
            visited.append(start)
            
            if arr[start] == 0:
                return True
            
            return dfs(start + arr[start]) or dfs(start - arr[start])
        
        return dfs(start)