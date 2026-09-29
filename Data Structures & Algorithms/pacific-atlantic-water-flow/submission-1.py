class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Creating visited sets
        pacific_visited = set()
        atlantic_visited = set()

        # Defining our directions
        directions = [
            (-1, 0), # up
            (1, 0),  # down
            (0, -1), # left
            (0, 1),  # right
        ]

        # Creating our recursive DFS function
        def DFS(row, col, visited_set):
            # Skip if we are out of bounds
            if row >= len(heights) or row < 0 or col >= len(heights[0]) or col < 0:
                return

            # Skip if we have already visited this cell
            if (row, col) in visited_set:
                return

            # Mark the cell as visited
            visited_set.add((row, col))

            # Traverse all possible directions
            for dr, dc in directions:
                # Getting our new position
                newRow = row + dr
                newCol = col + dc

                # Skip if we are out of bounds
                if newRow >= len(heights) or newRow < 0 or newCol >= len(heights[0]) or newCol < 0:
                    continue

                # Skip if we have visited this cell
                if (newRow, newCol) in visited_set:
                    continue

                # Skip if it is smaller
                if heights[newRow][newCol] < heights[row][col]:
                    continue

                # Recurse with our new information
                DFS(newRow, newCol, visited_set)

        # Call DFS on the top row for
        # pacific ocean
        for col in range(len(heights[0])):
            DFS(0, col, pacific_visited)

        # Call DFS on the left column for
        # pacific ocean
        for row in range(len(heights)):
            DFS(row, 0, pacific_visited)

        # Call DFS on the bottom row for
        # atlantic ocean
        for col in range(len(heights[0])):
            DFS(len(heights) - 1, col, atlantic_visited)

        # Call DFS on the right column for
        # atlantic ocean
        for row in range(len(heights)):
            DFS(row, len(heights[0]) - 1, atlantic_visited)

        # Return our answer via intersection
        return [[row, col] for row, col in (pacific_visited & atlantic_visited)]