"""
https://leetcode.com/problems/all-paths-from-source-to-target/

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        
        def traverse(origin, graph):
            
            if not graph[origin]:
                return []
            
            result = []
            for node in graph[origin]:
                path = [origin]
                if node == n - 1:
                    path.append(node)
                    result.append(path)
                else:
                    r = traverse(node, graph)
                    for x in r:
                        path = path + x
                        result.append(path)
                        path = [origin]
            return result
                        
        return traverse(0,graph)