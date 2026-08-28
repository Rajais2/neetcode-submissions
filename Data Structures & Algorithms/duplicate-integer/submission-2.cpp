class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> isDup;

        for (int i = 0; i < nums.size(); i++) {
            if (isDup.contains(nums[i])) {
                return true;
            } else {
                isDup.insert(nums[i]);
            }
        }

        return false;
    }
};