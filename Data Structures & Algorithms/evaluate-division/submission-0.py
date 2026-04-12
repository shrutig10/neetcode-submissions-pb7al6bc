class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # make a graph - undirected graph
        # edges will be weighted (a --> b will be 4, b --> a would be 0.25)
        # for each query, find a path from start to end and multiply as you go
        # if start or end does not exist in graph, -1
        # if path does not exist, return -1
        # dfs on all neighbors until you find one that works

        # if this node is the ending node --> return cur val (initialized to 1)
        # iterate through neighbors --> run dfs
        # if any of them do not return -1, return that
        # if all return -1, then return -1

        adj = defaultdict(list)

        for i in range(len(equations)):
            num, den = equations[i][0], equations[i][1]
            adj[num].append((den, values[i]))
            adj[den].append((num, 1 / values[i]))

        def dfs(cur, end, val):
            if cur in visited:
                return -1
            if cur == end:
                return val
            visited.add(cur)
            for nei in adj[cur]:
                quotient = dfs(nei[0], end, val * nei[1])
                if quotient != -1.0:
                    return quotient
        
            return -1.0

        res = []

        for num, den in queries:
            if num not in adj or den not in adj:
                res.append(-1.0)
            else:
                visited = set()
                res.append(dfs(num, den, 1))

        return res




        