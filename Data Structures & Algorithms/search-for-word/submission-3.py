class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # A simple way of representing all possible
        # movements
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        
        # Creating our DFS recursive function
        def DFS(row, col, word_index):
            # Checking if we are in bounds
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False

            # Checking if we have visited this cell already
            if board[row][col] == '#':
                return False

            # Checking if this cell doesn't match the
            # next part of our word
            if board[row][col] != word[word_index]:
                return False

            # We found the word!
            if word_index + 1 == len(word):
                return True

            # Marking this cell as visited
            original = board[row][col]
            board[row][col] = '#'

            # Traversing through all possible directions
            for dr, dc in directions:
                # Calculating our new row and col positions
                new_row = row + dr
                new_col = col + dc

                # We have found a cell for the next character
                if (DFS(new_row, new_col, word_index + 1)):
                    board[row][col] = original
                    return True

            # Tried all directions but none worked
            board[row][col] = original
            return False

        # Traversing through the board to find the first character
        for row in range(len(board)):
            for col in range(len(board[0])):
                # If we found the first character, begin exploring
                if board[row][col] == word[0]:
                    # Seeing if we can find the word
                    if DFS(row, col, 0):
                        return True

        # Checked all cells, meaning the word wasn't
        # found
        return False

