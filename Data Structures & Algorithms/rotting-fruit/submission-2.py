class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Define macros for readability sake
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        
        # Initializing necessary information
        numFreshOranges, totalWaves = 0, 0

        # Making our queue
        queue = deque()

        # Traverse the grid to collect information
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == FRESH:
                    # Increment the total amount of
                    # fresh oranges
                    numFreshOranges += 1
                elif grid[row][col] == ROTTEN:
                    # If it is a rotten orange, add its
                    # position to our queue
                    queue.append((row, col))

        # Defining our directions
        directions = [
            (-1, 0), # up
            (1, 0),  # down
            (0, -1), # left
            (0, 1),  # right
        ]

        # Attempt to keep processing oranges to rot
        while queue and numFreshOranges > 0:
            # Get the current wave size
            wave_size = len(queue)

            # Process all rotten orange in that wave
            for current_wave in range(wave_size):
                # Get the next rotten orange's position
                row, col = queue.popleft()

                # Explore all four directions
                for dr, dc in directions:
                    # Get new row and column positions
                    newRow = row + dr
                    newCol = col + dc

                    # Skip if we are out of bounds
                    if newRow >= len(grid) or newRow < 0 or newCol >= len(grid[0]) or newCol < 0:
                        continue

                    # If it is a fresh orange, rot it
                    if grid[newRow][newCol] == FRESH:
                        grid[newRow][newCol] = ROTTEN
                        numFreshOranges -= 1
                        queue.append((newRow, newCol))

            # We have now processed one wave
            totalWaves += 1

        # If we finished with fresh oranges left, then
        # it means it's impossible, otherwise, return
        # the total amount of minutes it took
        if numFreshOranges > 0:
            return -1
        else:
            return totalWaves