class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # looking for segments to be crushed
        # crushing the candies
        # drop the rest of the candies

        # set of candies to be crushed --> tuples of (r, c)
        # check for horizantal and vertical separately
        # horizantal --> second col to second to last col
        # vertical --> second row to second to last row
        # if it is surrounded by same cells as itself --> add all three to set
        # if our set is empty --> board in stable state return it

        # crushing --> take the set of tuples --> set their cells to 0

        # dropping --> for each col, traverse the rows in reverse order
        # save the last 0 (maximum row) --> once your encounter a row that does not a 0
        # swap that value with the max row with 0 and then decrement 0

        def look():
            crush = set()
            # horizontal
            for r in range(len(board)):
                for c in range(1, len(board[0]) - 1):
                    if board[r][c - 1] == board[r][c] == board[r][c + 1] and board[r][c] != 0:
                        crush.add((r, c - 1))
                        crush.add((r, c))
                        crush.add((r, c + 1))

            # vertical
            for c in range(len(board[0])):
                for r in range(1, len(board) - 1):
                    if board[r - 1][c] == board[r][c] == board[r + 1][c] != 0:
                        crush.add((r - 1, c))
                        crush.add((r, c))
                        crush.add((r + 1, c))

            return crush

        def crush(crush):
            for r, c in crush:
                board[r][c] = 0

        def drop():
            for c in range(len(board[0])):
                last_zero = -1
                for r in range(len(board) - 1, -1, -1):
                    if board[r][c] == 0:
                        last_zero = max(last_zero, r)
                    else:
                        board[r][c], board[last_zero][c] = board[last_zero][c], board[r][c]
                        last_zero -= 1

        to_crush = look()

        while to_crush:
            crush(to_crush)
            drop()
            to_crush = look()

        return board


        