class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # cycle detection algorithm --> dfs
        # everything must be one component --> start from any node you want
        # first make an adjacency list based off of edge list (know how many nodes exist)
        # if any element is empty, then return false, as it is a separate component
        # pick the first node in the list and then perform dfs
        # have a visited array --> if present, then return false
        # return true if size of visited array = n

        graph = [[] for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor != parent and not dfs(neighbor, node):
                        return False

            return True

        return dfs(0, -1) and len(visited) == n


        

        