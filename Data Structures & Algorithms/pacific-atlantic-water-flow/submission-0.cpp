class Solution {
public:
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};

    void DFS(vector<vector<int>>& heights, int row, int col, vector<vector<bool>>& visited) {
        // Checking our bounds and if we visited the cell already
        if (row < 0 || row >= heights.size() || col < 0 || col >= heights[0].size() || visited[row][col]) {
            return;
        }

        // Marking the cell as visited
        visited[row][col] = true;

        // Traversing all the adjacent cells
        for (int i = 0; i < 4; i++) {
            // Calculating the new row and column position
            int newRow = row + dx[i];
            int newCol = col + dy[i];

            // Checking if we're in bounds as well as if the
            // new height is greater than the previous height
            if (newRow >= 0 && newRow < heights.size() && newCol >= 0 && newCol < heights[0].size() &&
                heights[newRow][newCol] >= heights[row][col]) {
                // If all checks pass, explore that new adjacent cell
                DFS(heights, newRow, newCol, visited);
            }
        }
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        // Storing the size of the grid
        int m = heights.size();
        int n = heights[0].size();

        // Creating different visited 2D matrices for 
        // the pacific and atlantic oceans
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));

        // Creating a final vector to hold our answers
        vector<vector<int>> result;

        // Doing DFS on the top row (pacific ocean)
        for (int i = 0; i < m; i++) {
            DFS(heights, i, 0, pacific);
        }

        // Doing DFS on the left column (pacific ocean)
        for (int j = 0; j < n; j++) {
            DFS(heights, 0, j, pacific);
        }

        // Doing DFS on the bottom row (atlantic ocean)
        for (int i = 0; i < m; i++) {
            DFS(heights, i, n - 1, atlantic);
        }

        // Doing DFS on the right column (atlantic ocean)
        for (int j = 0; j < n; j++) {
            DFS(heights, m - 1, j, atlantic);
        }

        // Traversing through all rows and columns
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Checking for visited cells in BOTH 2D matrics
                if (pacific[i][j] && atlantic[i][j]) {
                    result.push_back({i, j});
                }
            }
        }

        // Returning the final result containing all positions
        return result;
    }
};