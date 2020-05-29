"""
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for x, y in prerequisites:
            nodes = [y]
            while nodes:
                node = nodes.pop(0)
                if x in graph[node]:
                    return False
                nodes.extend(graph[node])
            graph[x].append(y)
        
        return True