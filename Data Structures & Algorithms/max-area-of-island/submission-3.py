class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Will store the max area we find
        maxArea = 0

        # Defining all possible directions
        directions = [
            (-1, 0), # up
            (1, 0),  # down
            (0, -1), # left
            (0, 1),  # right
        ]

        # Create our DFS function
        def DFS(row, col):
            # Don't contribute if we are out of bounds
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return 0

            # Don't contribute if it's a water tile
            if grid[row][col] == 0:
                return 0

            # Mark it as visited (make it a water tile)
            grid[row][col] = 0

            # We know we have one island tile, so
            # we automatically have an area of 1
            area = 1

            # Explore all possible directions
            for dr, dc in directions:
                # Get our new row and column positions
                newRow = row + dr
                newCol = col + dc

                # Add any adjacent island tiles
                area += DFS(newRow, newCol)

            # Return the ultimate total area we find
            return area

        # Traverse through the board
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, DFS(row, col))

        # Return the max area we have found
        return maxArea