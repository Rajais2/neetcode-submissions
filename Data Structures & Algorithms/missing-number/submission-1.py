class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Getting the complete range (0 - n)
        n = len(nums)

        # Begin with n because the main
        # loop iterates through 0 and n - 1
        result = n

        # XOR each index with the number at that index
        for i in range(len(nums)):
            # Here, matching numbers will cancel and
            # the only number left will be the missing number
            result ^= i ^ nums[i]

        # Return the number that was missing
        return result