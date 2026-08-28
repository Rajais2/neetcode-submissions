class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Getting the dimensions of the matrix
        int m = matrix.size(), n = matrix[0].size();

        // Defining our two pointers
        int left = 0, right = (m * n) - 1;

        // Perform binary search
        while (left <= right) {
            // Calculate our middle index
            int mid = left + (right - left) / 2;

            // Getting the current position in the matrix
            int currentRow = mid / n, currentCol = mid % n;

            if (matrix[currentRow][currentCol] == target) {
                return true;
            } else if (matrix[currentRow][currentCol] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
    }
};
