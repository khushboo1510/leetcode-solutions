# https://leetcode.com/problems/clone-graph/
    
# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

# Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val                
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited = {}
        graph = Node()
        
        def dfs(node):
            if node:
                if node.val not in self.visited:
                    graph = Node(node.val)
                    self.visited[node.val] = graph
                    for neighbor in node.neighbors:
                        graph.neighbors.append(dfs(neighbor))
                    return graph
                else:
                    return self.visited[node.val]
        return dfs(node)
