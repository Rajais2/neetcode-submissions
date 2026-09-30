class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Preparing to use XOR
        result = 0

        # XOR our result with each number
        for num in nums:
            result ^= num

        # Return the integer that appears once
        return result