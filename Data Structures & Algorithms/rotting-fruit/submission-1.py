class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs 
        # get all the rotting fruit locations
        # whichever neighbors are fresh, make those rotten and add it to the queue
        # maintain a time which will be returned
        # go until the queue is empty

        queue = deque()
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))

        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                if r + 1 < len(grid) and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    queue.append((r + 1, c))
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    queue.append((r - 1, c))
                if c + 1 < len(grid[0]) and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    queue.append((r, c + 1))
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    queue.append((r, c - 1))
            if queue:
                time += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1

        return time

        