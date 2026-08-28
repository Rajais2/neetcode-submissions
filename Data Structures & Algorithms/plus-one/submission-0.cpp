class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1;

        // Start at the end of the vector
        for (int i = digits.size() - 1; i >= 0; i--) {
            // Getting the current sum by adding 1
            int curSum = digits[i] + carry;

            // If our current sum is over ten, reset it back to zero
            // and add to our carry
            if (curSum == 10) {
                digits[i] = 0;
                carry = 1;
            } else {
                // Otherwise, make the digit equal to our current sum
                digits[i] = curSum;

                // Reset our carry and stop
                carry = 0;
                break;
            }
        }

        // If we need a carry, insert a new digit
        if (carry == 1) {
            digits.insert(digits.begin(), 1);
        }

        // Return the vector after potentially modifying it
        return digits;
    }
};