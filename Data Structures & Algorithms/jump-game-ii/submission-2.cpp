class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() <= 1) {
            return 0;
        }

        int currentEnd = 0, furthestPos = 0, jumps = 0;

        for (int i = 0; i < nums.size() - 1; i++) {
            furthestPos = max(furthestPos, i + nums[i]);

            if (i == currentEnd) {
                jumps++;
                currentEnd = furthestPos;
            }
        }

        return jumps;
    }
};
