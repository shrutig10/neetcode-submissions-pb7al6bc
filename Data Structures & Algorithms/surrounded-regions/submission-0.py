class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # dfs
        # iterate through the board
        # if it's an o
        # run dfs
        # if we reach a border, then not surrounded by x, return false
        # if we encounter an x, surrounded at that point by x, return true
        # if another o, then continue dfs
        # go through visited and change all cells to x
        # dfs will tell us that we are surrounded

        def dfs(r, c, visited):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if (r, c) in visited or board[r][c] == 'X':
                return True
            visited.add((r, c))
            return dfs(r, c + 1, visited) and dfs(r + 1, c, visited) and dfs(r, c - 1, visited) and dfs(r - 1, c, visited)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    visited = set()
                    if dfs(r, c, visited):
                        for row, col in visited:
                            board[r][c] = 'X'
                    

        