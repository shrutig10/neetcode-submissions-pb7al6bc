class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # we only want to look at cells that are 1 --> exit if we see water (0)
        # maintain the largest area
        # iterate through the matrix --> if it's a 1, start of an island
        # check its neighbors --> dfs
        # if it is water, return, otherwise check that cell's neighbors, maintain the area 
        # base case --> if it's water or out of bounds or already visited, return
        # otherwise add to visited, then dfs on neighbors
        # return the sum of the area of neighbors
        # once dfs is completed, we will compare with largest area, and keep the max

        largest = 0
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 0
            if (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            cur_area = 1
            cur_area += dfs(r, c + 1)
            cur_area += dfs(r + 1, c)
            cur_area += dfs(r, c - 1)
            cur_area += dfs(r - 1, c)
            return cur_area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                largest = max(largest, dfs(r, c))

        return largest
                


        