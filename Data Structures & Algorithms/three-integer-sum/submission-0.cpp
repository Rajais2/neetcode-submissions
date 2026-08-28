#include <algorithm>

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // Will contain our future triplets
        vector<vector<int>> triplets;
        
        // Sorting the array
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size() - 2; i++) {
            // Skipping identical numbers
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            // Initializing our pointers
            int left = i + 1, right = nums.size() - 1;

            // Utilizing two pointer approach
            while (left < right) {
                // Calculating the current sum
                int sum = nums[i] + nums[left] + nums[right];

                // If the sum is zero, we found a triplet
                if (sum == 0) {
                    triplets.push_back({nums[i], nums[left], nums[right]});

                    // Move our pointers accordingly
                    left++;
                    right--;

                    // Skipping duplicates by repeatedly moving pointers if same number
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }

                    // Same logic here
                    while (right > left && nums[right] == nums[right + 1]) {
                            right--;
                    }
                } else if (sum < 0) {
                    // We need larger numbers so move left pointer up
                    left++;
                } else if (sum > 0) {
                    // We need smaller numbers so move right pointer up
                    right--;
                }
            }
        }

        // Returning the final unique triplets
        return triplets;
    }
};