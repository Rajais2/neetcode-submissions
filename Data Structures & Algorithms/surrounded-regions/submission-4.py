class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Defining our directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Storing information for readability sakes
        last_row = len(board) - 1
        last_col = len(board[0]) - 1

        # Creating our DFS recursive function
        def DFS(row, col):
            # Skip if we are out of bounds
            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
                return

            # Skip if it is not an 'O'
            if board[row][col] != "O":
                return

            # Mark the current cell as safe
            board[row][col] = "#"

            # Traversing all possible directions
            for dr, dc in directions:
                # Getting our new positions
                newRow = row + dr
                newCol = col + dc

                DFS(newRow, newCol)

        # DFS on the top row
        for col in range(len(board[0])):
            if board[0][col] == "O":
                DFS(0, col)

        # DFS on the left column
        for row in range(len(board)):
            if board[row][0] == "O":
                DFS(row, 0)

        # DFS on the bottom row
        for col in range(len(board[0])):
            if board[last_row][col] == "O":
                DFS(last_row, col)

        # DFS on the right column
        for row in range(len(board)):
            if board[row][last_col] == "O":
                DFS(row, last_col)

        # Traverse the board to flip non-safe
        # O spaces to Xs
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "#":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"