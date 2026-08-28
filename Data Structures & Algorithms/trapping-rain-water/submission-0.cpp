class Solution {
public:
    int trap(vector<int>& height) {
        // Setting up for two pointer approach
        int left = 0, right = height.size() - 1;

        int leftMaxHeight = INT_MIN, rightMaxHeight = INT_MIN;

        int totalAmount = 0;

        // Begin the tow pointer approach
        while (left < right) {
            if (height[left] < height[right]) {
                if (leftMaxHeight < height[left]) {
                    leftMaxHeight = height[left];
                } else {
                    totalAmount += leftMaxHeight - height[left];
                }

                left++;
            } else {
                if (rightMaxHeight < height[right]) {
                    rightMaxHeight = height[right];
                } else {
                    totalAmount += rightMaxHeight - height[right];
                }

                right--;
            }
        }

        return totalAmount;
    }
};
