class Solution {
public:
    // Making an array to represent directions
    // Specifically, up, down, left, and right
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};

    int DFS(vector<vector<int>>& grid, int row, int col) {
        int curLandArea = 1;
        
        if (row < 0 || row >= grid.size() || col < 0 || col >= grid[0].size()) {
            return 0;
        } else if (grid[row][col] == 0) {
            return 0;
        }

        grid[row][col] = 0;

        for (int i = 0; i < dx.size(); i++) {
            curLandArea += DFS(grid, row + dx[i], col + dy[i]);
        }

        return curLandArea;
    }
    
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxLength = 0, curLength = 0;

        for (int row = 0; row < grid.size(); row++) {
            for (int col = 0; col < grid[0].size(); col++) {
                if (grid[row][col] == 1) {
                    curLength = DFS(grid, row, col);
                    maxLength = max(maxLength, curLength); 
                }
            }
        }

        return maxLength;
    }
};
