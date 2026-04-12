class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # go through first column
        # once the number is larger, go back a column (or stay on the last column)
        # go through that row until you find the number, if you get to the end, return false
        i = 0
        while i < len(matrix) and matrix[i][0] <= target:
            if matrix[i][0] == target:
                return True
            i += 1
        
        i -= 1

        k = 0
        while k < len(matrix[i]) and matrix[i][k] <= target:
            if matrix[i][k] == target:
                return True
            k += 1
        
        return False