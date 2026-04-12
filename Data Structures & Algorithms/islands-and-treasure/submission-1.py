class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # iterate through matrix
        # skip land and water
        # process cells that are chests
        # change inf to minimum distance from chest
        # PROCESSING
        # multi source bfs
        # maintain a visited set
        # maintain a current distance
        # check four neighbors 
        # set the grid to the current distance

        visited = set()
        queue = deque()
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))

        cur_dist = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == -1 or (r, c) in visited:
                    continue
                visited.add((r, c))
                grid[r][c] = cur_dist
                queue.append((r - 1, c))
                queue.append((r, c - 1))
                queue.append((r + 1, c))
                queue.append((r, c + 1))
            cur_dist += 1
        

        