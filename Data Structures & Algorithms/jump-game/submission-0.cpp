class Solution {
public:
    bool canJump(vector<int>& nums) {
        int furthestPosition = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (i > furthestPosition) {
                return false;
            }

            furthestPosition = max(furthestPosition, i + nums[i]);
        }

        return true;
    }
};
