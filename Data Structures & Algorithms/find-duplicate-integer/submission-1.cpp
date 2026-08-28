class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // Using the slow and fast pointer approach
        int slow = nums[0];
        int fast = nums[0];

        // Keep moving the pointers until they collide
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        // Resetting our slow pointer to the beginning
        slow = nums[0];

        // Keep moving the pointers again until they collide
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }

        // Returning either pointer as they are at the duplicate number
        return slow;
    }
};
