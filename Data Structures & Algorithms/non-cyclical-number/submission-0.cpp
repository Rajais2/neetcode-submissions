class Solution {
public:
    bool isHappy(int n) {
        // Creating a set to see if we have a repeat
        unordered_set<int> seenNumbers;

        // Edge case: return true if it's already 1
        if (n == 1) {
            return true;
        }
    
        while (n != 1) {
            int sum = 0;

            while (n > 0) {
                int digit = n % 10;
                sum += pow(digit, 2);
                n = n / 10;
            }

            if (seenNumbers.contains(sum)) {
                return false;
            } else {
                seenNumbers.insert(sum);
            }

            n = sum;

            if (n == 1) {
                return true;
            }
        }

        return false;
    }
};
