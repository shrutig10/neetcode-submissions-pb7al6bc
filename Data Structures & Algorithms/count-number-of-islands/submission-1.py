class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # run a dfs 
        # as we explore all cells, mark visited ones by changing to 0
        # make sure you are in bounds during dfs
        # if the current cell is 0, return out
        # otherwise check for all neighbors
        # # of times dfs ran = # of islands
        # loop the grid, when you see a 1, start the dfs

        islands = 0

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
                return
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands
        