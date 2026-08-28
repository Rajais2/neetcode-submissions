class Solution {
public:
    int maxArea(vector<int>& height) {
        // Setting up our two pointers
        int left = 0, right = height.size() - 1;

        // Setting up to store the maximum calculated area
        int maxArea = 0;

        // Begin our two pointer approach
        while (left < right) {
            // The height is whatever column is smaller height wise
            int calcHeight = min(height[left], height[right]);

            // Getting the total distance between the two columns
            int width = right - left;

            // Calculating the current area with our calculations
            int area = calcHeight * width;

            // Updating our max area if it's greater
            maxArea = max(maxArea, area);

            // Advancing our pointers
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        // Returning the maximum area we calculated
        return maxArea;
    }
};