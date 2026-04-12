class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # if a self loop exists, then automatically return false
        # dfs 
        # if a path terminates, does it terminate at the destination
        # do any cycles exist? If a cycle exists, then return false

        # mark nodes as in progress and completed
        # if you encounter a node that is in progress, then it is a cycle, return false
        # if a node has been completed, then you can return true (all paths have been explored from this node)
        # if the node has no outgoing edges, then check that it is destination, otherwise return false
        
        # make adj list
        # start with the source --> mark grey to signify processing
        # explore paths, marking other nodes grey as we see (dfs on these nodes)
        # if we see a node with no outgoing edges, then check for destination and mark it black
        
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)

        PROCESSING = 1
        COMPLETED = 2

        def dfs(cur_node, destination, status):
            if status[cur_node] == PROCESSING or (not adj[cur_node] and cur_node != destination):
                return False
            if status[cur_node] == COMPLETED:
                return True
            status[cur_node] = PROCESSING

            for nei in adj[cur_node]:
                if not dfs(nei, destination, status):
                    return False

            status[cur_node] = COMPLETED
            
            return True

        return dfs(source, destination, [0] * n)

        
