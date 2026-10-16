class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Initialize our total perimeter
        totalPerimeter = 0

        # Create the directions we can move
        directions = [
            (-1, 0), # up
            (1, 0),  # down
            (0, -1), # left
            (0, 1)   # right
        ]

        # Traverse the board with nested loop as
        # there is only one connected island
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # Check what cell we're on
                if grid[row][col] == 0:
                    continue

                for dr, dc in directions:
                    # Calculate our new position
                    new_row = row + dr
                    new_col = col + dc

                    # Check if we are out of bounds
                    if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                        totalPerimeter += 1
                    elif grid[new_row][new_col] == 0:
                        totalPerimeter += 1

        # Return the total perimeter we calculated
        return totalPerimeter