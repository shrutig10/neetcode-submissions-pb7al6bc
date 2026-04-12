class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs
        # make an adjacency list 
        # check the neighbors
        # we will maintain a visited set for the dfs
        # iterate through the graph
        # if this node is not already in visited <-- run the dfs and increment our component count
        
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        components = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)

        for i in range(len(adj)):
            if i not in visited:
                dfs(i)
                components += 1
        
        return components

        