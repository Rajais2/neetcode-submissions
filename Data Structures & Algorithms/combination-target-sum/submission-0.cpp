class Solution {
public:
    vector<vector<int>> result;

    void backtrack(vector<int>& nums, vector<int>& path, int index, int target) {
        if (target == 0) {
            result.push_back(path);
            return;
        }

        for (int i = index; i < nums.size(); i++) {
            if (nums[i] > target) { 
                continue;
            } else {
                path.push_back(nums[i]);

                backtrack(nums, path, i, target - nums[i]);

                path.pop_back();
            }
        }
    }
    
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> path;

        backtrack(nums, path, 0, target);

        return result;
    }
};
