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
        
        visited = set()
        n = len(arr)
        queue = deque()
        queue += [start]
        while queue:
            index = queue.popleft()
            if index not in visited and index >= 0 and index < n:
                visited.add(index)
                if arr[index] == 0:
                    return True
                queue += [index - arr[index], index + arr[index]]
        return False
            
        
        #DFS Approach
        """
        self.visited = set()
        def jump(index, n):
            if index in self.visited or index < 0 or index >= n:
                return False
            self.visited.add(index)
            if arr[index] == 0:
                return True
            print(index, index - arr[index], index + arr[index])
            return jump(index - arr[index], n) or jump(index + arr[index], n)
    
        return jump(start, len(arr))
        """
