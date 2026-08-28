class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // Base case
        if (amount == 0) {
            return 0;
        }

        // Initializing our 1D table
        vector<int> dp(amount + 1, numeric_limits<int>::max());

        // Filling in the default values (the first cell will always be zero)
        dp[0] = 0;

        // Traversing to fill out all entries in our dynamic table
        for (int i = 1; i <= amount; i++) {
            // As well as traversing through all the coin values we have
            for (int coin : coins) {
                // If the transaction is valid, update the placement in our table if necessary
                if (i - coin >= 0 && dp[i - coin] != INT_MAX) {
                    dp[i] = min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        // Returning the amount of fewest number of coins needed
        return (dp[amount] == INT_MAX) ? -1 : dp[amount];
    }
};