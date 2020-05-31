"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

There are n cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [a, b] represents a road from city a to b.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach the city 0 after reorder.
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        outgoing = defaultdict(list)
        incoming = defaultdict(list)
        visited = [0] * n
        self.count = 0
        
        for x, y in connections:
            outgoing[x].append(y)
            incoming[y].append(x)
            
        visited[0] = 1
        
        def dfs(routes, flag):
            for city in routes:
                if not visited[city]:
                    visited[city] = 1
                    if flag:
                        self.count += 1
                    dfs(outgoing[city], True)
                    dfs(incoming[city], False)
                    
        dfs(outgoing[0], True)
        dfs(incoming[0], False)
        return self.count