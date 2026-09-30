class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # First transpose the matrix
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse all rows in our now
        # transposed matrix
        for row in range(len(matrix)):
            matrix[row].reverse()
