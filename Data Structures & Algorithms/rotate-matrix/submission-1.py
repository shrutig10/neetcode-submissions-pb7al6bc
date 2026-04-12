class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # switch the first and last rows of the matrix
        # transpose it
        # how to transpose --> switch the diagonals
        top, bottom = 0, len(matrix) - 1

        while top < bottom:
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            top += 1
            bottom -= 1

        for r in range(len(matrix)):
            for c in range(r, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


        