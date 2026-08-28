class Solution {
public:
    // Creating a global tracker for all permutations
    vector<vector<int>> result;

    // This is our backtracking function
    void backtrack(vector<int>& nums, vector<int>& path, vector<bool>& usage) {
        // If we have reach a full permutation, we stop recursing
        if (path.size() == nums.size()) {
            result.push_back(path);
            return;
        }

        // Traverse through all elements
        for (int i = 0; i < nums.size(); i++) {
            // Checking if we have this particular element
            if (usage[i] == false) {
                // Add this current path and mark it as used
                path.push_back(nums[i]);
                usage[i] = true;

                // Perform some backtracking
                backtrack(nums, path, usage);

                // Undo our choice and mark the current element as unused
                path.pop_back();
                usage[i] = false;
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        // Intializing necessary containers
        vector<int> path;
        vector<bool> usage(nums.size(), false);

        // Call our recursive algorithm
        backtrack(nums, path, usage);

        // Return all permutations
        return result;
    }
};