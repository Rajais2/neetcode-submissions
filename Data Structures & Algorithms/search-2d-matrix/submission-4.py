class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Set up the left and right pointers
        left, right = 0, len(matrix) * len(matrix[0]) - 1

        # Extracting the number of columns and rows
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # Start performing binary search
        while left <= right:
            # Calculate our mid
            mid = (left + right) // 2

            # Getting our mid's row and column position
            rowPos = mid // num_cols
            colPos = mid % num_cols

            # Performing various checks
            if (matrix[rowPos][colPos] == target):
                return True
            elif (matrix[rowPos][colPos] < target):
                left = mid + 1
            elif (matrix[rowPos][colPos] > target):
                right = mid - 1

        return False