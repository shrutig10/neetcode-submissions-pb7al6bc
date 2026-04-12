class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for each rule separately
        # use a hashset to keep track of which numbers we've seen (reset the set each loop)
        # to check the squares - outer loop running 3 times, row loop running 0-2, 3-5, 6-8
        # column going from 0-8
        # proper row index = outer loop * 3 + row

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

        for i in range(len(board) // 3):
            for c in range(len(board[0])):
                if c % 3 == 0:
                    seen = set()
                for r in range(len(board) // 3):
                    if board[i * 3 + r][c] == '.':
                        continue
                    if board[i * 3 + r][c] in seen:
                        return False
                    seen.add(board[i * 3 + r][c])

        return True
                




        

        