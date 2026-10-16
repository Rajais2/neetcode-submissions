# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Create our two pointers (range is 1 - n)
        left = 1
        right = n

        # Perform binary search!!!!!!!
        while left <= right:
            # Calculuate our guess
            guessNum = (left + right) // 2

            # Obtain our result
            result = guess(guessNum)

            # Act accordingly based on the results
            if result == 0:
                return guessNum
            elif result == -1:
                right = guessNum - 1
            elif result == 1:
                left = guessNum + 1

        return -1