class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // Setting up our two pointers
        int left = 0, right = numbers.size() - 1;

        // Begin the two pointers approach
        while (left < right) {
            // Calculating our current sum
            int total = numbers[left] + numbers[right];

            // If our sum matches the target, return the indices (one-indexed)
            if (total == target) {
                return {left + 1, right + 1};
            } else if (total < target) {
                // We need bigger numbers so move left pointer up
                left++;
            } else {
                // Otherwise, we need smaller numbers so move right pointer down
                right--;
            }
        }
    }
};
