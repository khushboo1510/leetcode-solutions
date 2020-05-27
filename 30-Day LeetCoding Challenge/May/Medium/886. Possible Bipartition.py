"""
https://leetcode.com/problems/possible-bipartition/

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.
"""

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        for i in graph.keys():
            if i not in visited:
                queue = collections.deque([i])
                while queue:
                    groupl = set(queue)
                    for j in range(len(queue)):
                        cur = queue.popleft()
                        visited.add(cur)
                        for x in graph[cur]:
                            if x in groupl: return False
                            if x not in visited: queue.append(x)
        return True   