class Solution {
public:
    int findMin(vector<int>& nums) {
        // Setting up for classic binary search
        int left = 0, right = nums.size() - 1;

        // Keep performing binary search until we haven't converged
        while (left != right) {
            // Calculating our middle position
            int mid = (left + right) / 2;

            // Checking if our minimum is on the right side (excluding mid)
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                // Otherwise, it is on the left side (including mid)
                right = mid;
            }
        }

        // Return the minimum value
        return nums[left];
    }
};