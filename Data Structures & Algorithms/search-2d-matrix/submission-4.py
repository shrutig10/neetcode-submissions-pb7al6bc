class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        # look at the first column of every row and do a binary search on that
        # choose row that is less than or equal to the target and closest to it
        # do a binary search on that row for the target

        u, d = 0, len(matrix) - 1
        while u <= d:
            mid = (u + d) // 2
            if matrix[mid][-1] < target:
                u = mid + 1
            elif matrix[mid][0] > target:
                d = mid - 1
            else:
                break

        l, r = 0, len(matrix[0]) - 1
        row = (u + d) // 2

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
        