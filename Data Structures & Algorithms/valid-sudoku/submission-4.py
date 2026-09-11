class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Making a dictionaries of sets for the rows,
        # columns, and each square
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # Begin traversing each cell in the sudoku board
        for row in range(9):
            for col in range(9):
                # Get the current cell
                curCell = board[row][col]

                # Skip if it's an empty cell
                if curCell == ".":
                    continue

                # Getting the square the cell belongs to
                squarePos = (row // 3) * 3 + (col // 3)

                if curCell in rows[row] or curCell in cols[col] or curCell in squares[squarePos]:
                    return False

                rows[row].add(curCell)
                cols[col].add(curCell)
                squares[squarePos].add(curCell)

        return True
