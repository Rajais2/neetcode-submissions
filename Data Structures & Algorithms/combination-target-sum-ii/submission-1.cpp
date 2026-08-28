class Solution {
public:
    // Creating a global variable to hold the final result
    vector<vector<int>> result;

    // Here is our backtracking function
    void backtrack(vector<int>& candidates, vector<int>& path, int index, int target) {
        // If our target is now zero, the path we're on is a candidate
        if (target == 0) {
            result.push_back(path);
            return;
        }

        // Otherwise, we have to explore all of the next possibilities
        for (int i = index; i < candidates.size(); i++) {
            // Skip any numbers that are larget than our target
            if (candidates[i] > target) { 
                break;
            } else if (candidates[i] == candidates[i - 1] && i > index) {
                continue;
            } else {
                // Temporarily add the number
                path.push_back(candidates[i]);

                // Recurse on that specific digit
                backtrack(candidates, path, i + 1, target - candidates[i]);

                // Undo our choice
                path.pop_back();
            }
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        
        // Setting up to store the current path we're on
        vector<int> path;

        // Calling our backtracking recursive function
        backtrack(candidates, path, 0, target);

        // Returning the final result
        return result;
    }
};
