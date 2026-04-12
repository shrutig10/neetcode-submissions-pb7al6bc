class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # iterate through the board
        # once we find a letter that is the beginning of word
        # perform a dfs
        # target letter that we're looking for and check that the neighbors are that letter
        # need to have an index that goes through word to get target letter
        # cur string <- if the string is not the word we're looking for/longer than what we want return

        seen = set()

        def dfs(r, c, target):
            if target >= len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or (r, c) in seen or board[r][c] != word[target]:
                return False
            seen.add((r, c))
            res = dfs(r, c + 1, target + 1) or dfs(r + 1, c, target + 1) or dfs(r, c - 1, target + 1) or dfs(r - 1, c, target + 1)
            seen.remove((r, c))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True

        return False
        