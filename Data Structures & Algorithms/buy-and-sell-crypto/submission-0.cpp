#include <climits>

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // Setting up to store the minimum price
        int min_price = INT_MAX;
        int max_profit = 0;

        // Traverse through our prices
        for (int i = 0; i < prices.size(); i++) {
            // If the current price is less than the minimum price, update it
            if (prices[i] < min_price) {
                min_price = prices[i];
            } else {
                // Otherwise, calculate the current profit gained
                int profit = prices[i] - min_price;

                // If the current profit is more than the max seen profit, update it
                if (profit > max_profit) {
                    max_profit = profit;
                }
            }
        }

        // Return the max profit in the end
        return max_profit;
    }
};