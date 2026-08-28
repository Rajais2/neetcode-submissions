class Solution {
public:
    int minDistance(string word1, string word2) {
        // Creating a two-dimensional table to hold up all of our costs
        vector<vector<int>> dp(word1.size() + 1, vector<int>(word2.size() + 1, 0));

        // Filling in what we know (first row is simply incrementing by 1)
        for (int j = 0; j < dp[0].size(); j++) {
            dp[0][j] = j;
        }

         // Filling in what we know (first column is simply incrementing by 1)
        for (int i = 0; i < dp.size(); i++) {
            dp[i][0] = i;
        }

        // Traversing through all the characters in both strings
        for (int i = 1; i <= word1.size(); i++) {
            for (int j = 1; j <= word2.size(); j++) {
                // If our characters match, no work is needed, meaning no cost
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    // Otherwise, we take the minimum cost of all operations
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, (min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)));
                }
            }
        }

        // The final cell in our table holds the minimum edit distance
        return dp[word1.size()][word2.size()];
    }
};