class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Defining a macro for readability sake
        INF = 2147483647

        # Make our queue for BFS
        queue = deque()

        # Defining directions for clarity
        directions = [
            (-1, 0), # up
            (1, 0),  # down
            (0, -1), # left
            (0, 1),  # right
        ]

        # Traverse the board to store treasure spots
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # Add the treasures position
                if grid[row][col] == 0:
                    queue.append((row, col))

        # Keep performing BFS!!!!!!
        while queue:
            # Get the next treasure position
            curRow, curCol = queue.popleft()
            
            # Get that position's current distance
            currentDist = grid[curRow][curCol]

            # Explore all four directions from the current cell
            for dr, dc in directions:
                # Get our new position
                newRow = curRow + dr
                newCol = curCol + dc

                # Skip if we are out of bounds
                if newRow >= len(grid) or newRow < 0 or newCol >= len(grid[0]) or newCol < 0:
                    continue

                # Skip over water and already visited tiles
                if grid[newRow][newCol] == -1 or grid[newRow][newCol] != INF:
                    continue

                # Update the grid in place and add its
                # position to our queue
                grid[newRow][newCol] = currentDist + 1
                queue.append((newRow, newCol))