class Solution {
public:
    const int WATER = -1;
    const int CHEST = 0;
    const int INF = 2147483647;

    // Creating a vector to represent all the total different directions
    vector<int> directionRow = {-1, 1, 0, 0};
    vector<int> directionCol = {0, 0, -1, 1};

    void islandsAndTreasure(vector<vector<int>>& grid) {
        // Setting up a queue to perform BFS
        queue<tuple<int, int, int>> BFSQueue;

        // Traversing the grid to store all positions of the chests
        for (int row = 0; row < grid.size(); row++) {
            for (int col = 0; col < grid[0].size(); col++) {
                if (grid[row][col] == CHEST) {
                    // Pushing all the chests, specifically their positions
                    BFSQueue.push({row, col, 0});
                }
            }
        }

    
        // Beginning the BFS process
        while (!BFSQueue.empty()) {
            // Popping and storing the next chest
            auto [row, col, dist] = BFSQueue.front();
            BFSQueue.pop();

            for (int i = 0; i < directionRow.size(); i++) {
                int newRow = row + directionRow[i], newCol = col + directionCol[i];

                if (newRow >= 0 && newRow < grid.size() && newCol >= 0 && newCol < grid[0].size()) {
                    if (grid[newRow][newCol] == INF) {
                        grid[newRow][newCol] = dist + 1;
                        BFSQueue.push({newRow, newCol, dist + 1});
                    }
                }
            }
        }
    }
};
