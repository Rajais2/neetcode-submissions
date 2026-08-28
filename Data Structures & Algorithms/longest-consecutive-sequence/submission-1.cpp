class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // Creating our set to help with tracking
        unordered_set<int> numsSet;

        int counter = 0, maxLength = 0;

        // Build our set
        for (int i = 0; i < nums.size(); i++) {
            numsSet.insert(nums[i]);
        }

        for (int curNum : numsSet) {
            auto it = numsSet.find(curNum - 1);

            if (it != numsSet.end()) {
                continue;
            } else {
                counter = 1;

                while (numsSet.contains(curNum + 1)) {
                    counter++;
                    curNum += 1;
                }

                maxLength = max(maxLength, counter);
            }
        }

        return maxLength;
    }
};
