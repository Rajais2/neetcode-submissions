class Solution {
public:
    // Creating a global variable to hold all subsets
    vector<vector<int>> result;

    void backtrack(vector<int>& nums, int index, vector<int>& path) {
        // Add the valid current path we're on
        result.push_back(path);
            
        // Move to each remaining element (ensuring we move forward and avoid duplicates)
        for (int i = index; i < nums.size(); i++) {
            // Include the current element in the current subset
            path.push_back(nums[i]);

            // Move forward and build more subsets, ensuring we don't reuse elements
            backtrack(nums, i + 1, path);

            // Here, we backtrack here by undoing our choice of inserting the current element
            path.pop_back();
        }
    }
    
    // The actual function
    vector<vector<int>> subsets(vector<int>& nums) {
        // Setting up to store the curent subset
        vector<int> path;

        // Start the backtracking with an empty subset and the zeroth index
        backtrack(nums, 0, path);

        // Returning the final result
        return result;
    }
};