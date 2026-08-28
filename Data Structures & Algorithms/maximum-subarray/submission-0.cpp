class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // Setting up to use Kadane's algorithm
        int currentResult = nums.at(0), maxResult = nums.at(0);

        // Begin our traversal of the nums vector
        for (int i = 1; i < nums.size(); i++) {
            // Here, we ask if it's better to continue the subarray
            // or either restart 
            currentResult = max(nums[i], currentResult + nums[i]);

            // Here, we simply check if we have a higher sum
            maxResult = max(maxResult, currentResult);
        }

        // Return the biggest sum we encountered
        return maxResult;
    }
};
