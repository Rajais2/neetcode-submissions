class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Represents the total amount of islands
        totalIslands = 0

        # Creating all possible directions we can travel
        directions = [
            (-1, 0), # up
            (1, 0),  # down
            (0, -1), # left
            (0, 1)   # right
        ]

        # Creating our DFS function
        def DFS(row, col):
            # Stop if we are out of bounds
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return

            # Stop if we launch on water
            if grid[row][col] == "0":
                return

            # Mark it as visited (make it water)
            grid[row][col] = "0"

            # Explore all possible directions
            for dr, dc in directions:
                # Getting our new row and col positions
                new_row = row + dr
                new_col = col + dc

                DFS(new_row, new_col)

        # Traverse the board to find islands
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # Found a new piece of land
                if grid[row][col] == "1":
                    totalIslands += 1
                    DFS(row, col)

        # Return the number of islands we found
        return totalIslands

            