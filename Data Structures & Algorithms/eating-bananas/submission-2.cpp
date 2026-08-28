class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // Defining our pointers
        int left = 1, right = *max_element(piles.begin(), piles.end());
        
        // And defaulting our current answer
        int answer = right;

        // Begin the binary search operation
        while (left <= right) {
            // Calculating mid and setting up to sum total hours
            int mid = left + (right - left) / 2;
            int totalHours = 0;

            // Go through each pile and sum the total hours 
            // at the eating speed
            for (int pile : piles) {
                totalHours += ceil((double) pile / mid);
            }

            // Performing many checks
            if (totalHours <= h) {
                // If we can eat it under the specific hourly rate, it is
                // a valid answer but we still look for other smaller options
                answer = mid;
                right = mid - 1;
            } else {
                // Otherwise, it is not a valid option and we look for bigger options
                left = mid + 1;
            }
        }

        // Returning the minimum eating rate
        return answer;
    }
};