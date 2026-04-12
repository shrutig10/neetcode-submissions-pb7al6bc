class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # first check every row
        # check every col
        # create a set to check for duplicates
        # double for loop
        # range(0-2), i will be 0-2,
        # array of hashmaps
        # index of square will be row / 3 * 3 + col / 3
        

        for r in range(len(board)):
            seen = set()
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for c in range(len(board[0])):
            seen = set()
            for r in range(len(board)):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        seenArray = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seenArray[(r // 3) * 3 + (c // 3)]:
                    return False
                seenArray[(r // 3) * 3 + (c // 3)].add(board[r][c])
        
        return True

        