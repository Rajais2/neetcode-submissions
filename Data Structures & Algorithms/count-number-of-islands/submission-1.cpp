class Solution {
public:
    // Making an array to represent directions
    // Specifically, up, down, left, and right
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};
    
    void DFS(vector<vector<char>>& grid, int row, int col) {
        // Bounds checking so we stop
        if (row < 0 || row >= grid.size() || col < 0 || col >= grid[0].size()) {
            return;
        } else if (grid[row][col] == '0') {
            // Stop since it's a water tile as well
            // This will be our way of marking visited tiles too
            return;
        }

        // Mark the current cell as visited by turning
        // it into a water tile
        grid[row][col] = '0';

        // Explore all adjacent cells
        for (int i = 0; i < dx.size(); i++) {
            DFS(grid, row + dx[i], col + dy[i]);
        }
    }
    
    int numIslands(vector<vector<char>>& grid) {
        // Tracking the total number of islands
        int totalIslands = 0;

        // Traversing the entire board
        for (int row = 0; row < grid.size(); row++) {
            for (int col = 0; col < grid[0].size(); col++) {
                // Check if the current cell is an island
                if (grid[row][col] == '1') {
                    // If it is, increment total islands and explore
                    totalIslands++;
                    DFS(grid, row, col);
                }
            }
        }

        // Return the total number of islands found
        return totalIslands;
    }
};
