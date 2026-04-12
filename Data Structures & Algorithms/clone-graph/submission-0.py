"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # need to visit all nodes to copy them and get their neighbors
        # bfs
        # use a map for visited
        # keep track of nodes we have visited and ensure that we are reusing the same nodes

        # have a queue and add nodes to it
        # if the node exists in the map already, then use it to get neighbors
        # if the node does not exist, create it and add its neighbors to the queue if they are not already in the map
        # map old nodes to new nodes

        hashmap = {}

        def dfs(node):
            if not node:
                return None
            if node in hashmap:
                return hashmap[node]
            
            new_node = Node(node.val)
            hashmap[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))

            return new_node

        return dfs(node)
        

       


        