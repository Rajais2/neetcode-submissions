class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()

            for cell in row:
                if cell == ".":
                    continue

                if cell in seen:
                    return False

                seen.add(cell)

        # Check columns
        for col in range(9):
            seen = set()

            for row in range(9):
                cell = board[row][col]

                if cell == ".":
                    continue

                if cell in seen:
                    return False

                seen.add(cell)

        # Check 3x3 squares
        for square in range(9):
            seen = set()

            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    cell = board[row][col]

                    if cell == ".":
                        continue

                    if cell in seen:
                        return False

                    seen.add(cell)

        return True
