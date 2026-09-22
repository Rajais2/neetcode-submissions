class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Representing the initial board state (n * n)
        board = [["."] * n for _ in range(n)]

        # Will hold the final answer
        result = []

        # Creating all the necessary sets we need
        columns = set()
        diag_positive = set()
        diag_negative = set()

        # Creating our recursive backtracking function
        def DFS(curRow):
            if curRow == len(board):
                # Convert each row to a string and
                # add it to our final answer
                result.append(["".join(row) for row in board])
                return
            
            # Traverse through each column in the row
            for col in range(n):
                # Skip this position if we have a conflict
                if col in columns or curRow + col in diag_positive or curRow - col in diag_negative:
                    continue

                # Place the queen
                board[curRow][col] = "Q"

                # Add the necessary information to our sets
                columns.add(col)
                diag_positive.add(curRow + col)
                diag_negative.add(curRow - col)

                # Explore this new queen placement
                DFS(curRow + 1)

                # Undo everything
                board[curRow][col] = "."
                columns.discard(col)
                diag_positive.discard(curRow + col)
                diag_negative.discard(curRow - col)

        # Begin exploring with the first row
        DFS(0)

        # Return our final answer
        return result   