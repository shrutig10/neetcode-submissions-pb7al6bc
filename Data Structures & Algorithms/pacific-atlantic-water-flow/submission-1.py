class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # need to check that they can reach the edges
        # check neighbors --> dfs
        # for each cell, check that they either border an edge or can reach an edge (meaning neighbors are less than or equal)
        # rather than check for cells that can reach the ocean, we can check for cells the ocean can reach
        # cells that the ocean is guaranteed to reach --> edge cells
        # from there, do a dfs to check how far the oceans can go in
        # we have to do dfs for each bordering cell 
        # separate lists to store which cells the pacific/atlantic can reach

        # two sets --> pacific cells, atlantic cells
        # initialize them with guaranteed cells (border)
        # for each of these lists, for each cell in the list, do a dfs and add any cell that can be reached
        # check will be that the neighbor has to be greater than or equal to the current cell
        # make sure to have a visited set for dfs
        # check for out of bounds --> once reached out of bounds then add it to the list of reachable cells
        # compare two lists, and see which elements are in both

        pacific, atlantic = set(), set()

        def dfs(r, c, oldHeight, reachable):
            if r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]):
                return 
            if (r, c) in reachable or heights[r][c] < oldHeight:
                return
            reachable.add((r, c))
            dfs(r, c + 1, heights[r][c], reachable)
            dfs(r + 1, c, heights[r][c], reachable)
            dfs(r, c - 1, heights[r][c], reachable)
            dfs(r - 1, c, heights[r][c], reachable)


        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0:
                    dfs(r, c, 0, pacific)
                if r == len(heights) - 1:
                    dfs(r, c, 0, atlantic)
                if c == 0:
                    dfs(r, c, 0, pacific)
                if c == len(heights[0]) - 1:
                    dfs(r, c, 0, atlantic)


        res = []
        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r, c])

        return res








        