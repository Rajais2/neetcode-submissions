class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Use booleans to track if the first
        # column or row has a zero
        firstRowZero = False
        firstColZero = False

        # Checking the first row
        firstRowZero = any(cell == 0 for cell in matrix[0])

        # Now checking the first column
        firstColZero = any(row[0] == 0 for row in matrix)

        # Now traverse the rest of the matrix to mark cells
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                # If we encounter a zero, set the
                # marker cells to zero as well
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Now traverse the rest of the matrix
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                # If our marker cells have a zero, change the
                # current cell to a zero
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # Zero out cells if the first row has a zero
        if firstRowZero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0

        # Zero out cells if the first column has a zero
        if firstColZero:
            for row in range(len(matrix)):
                matrix[row][0] = 0