class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # if neighbor is not land, add to perimeter (out of bounds/water)
        # dfs
        # iterate until we find land

        # base case: out of bounds --> return 1
        # base case: if cell is water --> return 1
        # if cell is visited: return 0
        # add cell to visited
        # perimeter = 0
        # add results of dfs of all neighbors (4 directions) to perimeter
        # return perimeter

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            visited.add((r, c))

            perimeter = 0
            perimeter += dfs(r, c + 1)
            perimeter += dfs(r + 1, c)
            perimeter += dfs(r, c - 1)
            perimeter += dfs(r - 1, c)

            return perimeter

            

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    visited = set()
                    return dfs(r, c)

        