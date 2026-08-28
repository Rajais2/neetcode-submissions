class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        // Creating our two dimensional table
        vector<vector<int>> dp(text1.size() + 1, vector<int>(text2.size() + 1, 0));

        // Filling in information we know
        for (int j = 0; j < dp[0].size(); j++) {
            dp[0][j] = 0;
        }

        // Filling in information we know
        for (int i = 0; i < dp.size(); i++) {
            dp[i][0] = 0;
        }

        // Traversing through our strings
        for (int i = 1; i <= text1.size(); i++) {
            for (int j = 1; j <= text2.size(); j++) {
                // If our character matches, copy the value while incrementing it
                if (text1[i - 1] == text2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    // Otherwise, take the maximum of the adjacent cells
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);   
                }
            }
        }

        // The final cell should have the answer
        return dp[text1.size()][text2.size()];
    }
};