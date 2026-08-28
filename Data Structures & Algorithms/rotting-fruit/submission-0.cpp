class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        // Tracking the remaining fresh oranges
        int freshOrangesRemaining = 0;

        // Tracking the total number of minutes that passed
        int totalMinutes = 0;

        // Tracking the current wave size (number of rotten oranges per iteration)
        int currentWaveSize = 0;

        // Adding a flag to indicate whether an orange was rotten
        bool infected = false;

        // Creating our queue to perform multisource BFS
        queue<pair<int, int>> BFSQueue;

        // Performing an initial scan to set up everything
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                // If we encounter a rotten orange, add to the queue
                // as it is one of the possible starting positions 
                if (grid[i][j] == 2) {
                    BFSQueue.push({i, j});
                } else if (grid[i][j] == 1) {
                    // If we encounter a fresh orange, we increment our
                    // total amount of fresh oranges
                    freshOrangesRemaining++;
                }
            }
        }

        // Handling edge cases
        if (freshOrangesRemaining == 0) {
            // If there are no fresh oranges, return -1
            return 0;
        } else if (BFSQueue.empty() && freshOrangesRemaining > 0) {
            // If there are fresh oranges remaining but no infection 
            // starting points, return -1
            return -1;
        }

        // Creating a vector to represent all the total different directions
        vector<int> directionRow = {-1, 1, 0, 0};
        vector<int> directionCol = {0, 0, -1, 1};

        // Begin processing all the rotten oranges
        while (!BFSQueue.empty()) {
            // Get the current wave size and a flag to see if we have infected an orange
            currentWaveSize = BFSQueue.size();
            infected = false;

            for (int i = 0; i < currentWaveSize; i++) {
                // Get the top rotten orange from our queue
                auto orangeCell = BFSQueue.front();
                BFSQueue.pop();

                for (int i = 0; i < directionRow.size(); i++) {
                    // Get all neighboring oranges' positions
                    int newRow = orangeCell.first + directionRow[i], newCol = orangeCell.second + directionCol[i];
                    
                    // Bounds checking
                    if (newRow >= 0 && newRow < grid.size() && newCol >= 0 && newCol < grid[0].size()) {
                        // Infect the adjacent orange if it is fresh and do all steps accordingly
                        if (grid[newRow][newCol] == 1) {
                            grid[newRow][newCol] = 2;
                            infected = true;
                            BFSQueue.push({newRow, newCol});
                            freshOrangesRemaining--;
                        }
                    }
                }
            }

            // If we have infected oranges, increaes the total number of minutes
            if (infected) {
                totalMinutes++;
            }
        }

        // Checking if all oranges were infected
        // If they were, return the total number of elasped minutes or -1
        if (freshOrangesRemaining > 0) {
            return -1;
        } else {
            return totalMinutes;
        }
    }
};