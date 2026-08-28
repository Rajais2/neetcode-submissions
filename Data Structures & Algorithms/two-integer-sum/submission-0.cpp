class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Using the hash table approach
        unordered_map<int, int> numMap;

        // Begin the traversal
        for (int i = 0; i < nums.size(); i++) {
            // Getting the complement (subtraction)
            int complement = target - nums[i];

            // Checking if our map contains the target
            if (numMap.contains(complement)) {
                // If so, return both indices
                return {numMap[complement], i};
            }

            // Storing the number in our hashmap
            numMap[nums[i]] = i;
        }

        // Return nothing if none was found
        return {};
    }
};
