class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs
        # iterate through the board
        # send in an index
        # if this letter is equal to the first letter of the word
        # start dfs
        
        # base case: if you reached end of the word, return true
        # if the current letter in the matrix is not what you're looking for or if visited, return false
        # check that any of the neighbors are the next letter (dfs on 4 sides)
        # keep visited set (r, c)
        # once you finish looking through the neighbors, remove the letter from visited

        visited = set()

        def dfs(index, r, c):
            if index == len(word):
                return True
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]): 
                return False
            if (r, c) in visited or board[r][c] != word[index]:
                return False
            
            visited.add((r, c))
            if dfs(index + 1, r, c + 1) or dfs(index + 1, r + 1, c) or dfs(index + 1, r, c - 1) or dfs(index + 1, r - 1, c):
                return True
            visited.remove((r, c))
            return False
            
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(0, r, c):
                    return True

        return False


        