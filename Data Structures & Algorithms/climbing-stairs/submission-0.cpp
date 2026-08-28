class Solution {
public:
    int climbStairs(int n) {
        // Checking for base case
        if (n <= 2) {
            return n;
        }
        
        // Creating a cache to store all our of prior answers
        vector<int> cache(n + 1, 0);

        // Prefilling the simple cases in our cache
        // The first spot should be zero as it takes zero steps to get there
        cache[1] = 1;
        cache[2] = 2;

        // Begin the traversal to fill up the rest of our cache
        for (int i = 3; i <= n; i++) {
            // The general pattern here is that we sum up the number of steps
            // one and two steps prior to the current step
            cache[i] = cache[i - 1] + cache[i - 2];
        }

        // Our answer lies in the last cell of our cache
        return cache[n];
    }
};