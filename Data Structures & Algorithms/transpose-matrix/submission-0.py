class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Get the number of rows of columns
        rows = len(matrix)
        cols = len(matrix[0])

        # Will hold the final tranposed result
        result = []

        # Traverse through the columns
        for i in range(cols):
            # Will hold the transposed column
            row = []

            # Go through the whole column and add 
            # the values
            for j in range(rows):
                row.append(matrix[j][i])

            # Finally, append the transposed row
            result.append(row)

        # Return the transposed matrix
        return result