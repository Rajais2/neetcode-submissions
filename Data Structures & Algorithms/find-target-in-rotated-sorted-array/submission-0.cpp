class Solution {
public:
    int search(vector<int>& nums, int target) {
        // Search the classics for binary search
        int left = 0, right = nums.size() - 1;

        // Perform the classic binary search
        while (left <= right) {
            // Calculate the middle position
            int mid = (left + right) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // Checking if the left side is ascending, meaning it is left rotated
            if (nums[left] <= nums[mid]) {
                // Checking if the target is within the left sorted side
                // If so, head left
                if ((nums[left] <= target) && (target <= nums[mid])) {
                    // Move the right pointer
                    right = mid - 1; 
                } else {
                    // Otherwise, move the left pointer up
                    left = mid + 1;
                }
            } else {
                if ((nums[mid] <= target) && (target <= nums[right])) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        // Returning -1 if the target is not found
        return -1;
    }
};