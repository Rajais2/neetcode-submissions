class Solution {
public:
    int search(vector<int>& nums, int target) {
        // Creating up pointers for binary search
        int left = 0, right = nums.size() - 1;

        // Begin our binary search traversal
        while (left <= right) {
            // Calculate our middle index
            int mid = left + (right - left) / 2;

            // Returning mid if it matches the target value
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        // In the end, both the left and right pointer will be the index
        // of the peak
        return -1;
    }
};