class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        # if we see a 0, then we can continue, or if out of bounds, continue
        # need to keep running count of all islands
        # if we see a 1, then we need to check neighbors
        # keep track of cells that we've visited

        # iterate through the grid
        # if 0, skip
        # if visited, skip
        # if i see a 1, then run dfs and add one to island counter

        # within dfs
        # check if 0, return
        # if visited, return
        # if 1, then check its neighbors (run dfs on that)

        # return the island counter

        visited = set()
        island_count = 0

        def dfs(grid, row, col, visited):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0' or (row, col) in visited:
                return
            visited.add((row, col))

            dfs(grid, row + 1, col, visited)
            dfs(grid, row, col + 1, visited)
            dfs(grid, row - 1, col, visited)
            dfs(grid, row, col - 1, visited)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '0' or (r, c) in visited:
                    continue
                dfs(grid, r, c, visited)
                island_count += 1

        return island_count
        
        