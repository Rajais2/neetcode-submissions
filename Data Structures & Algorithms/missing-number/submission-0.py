class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n

        for i in range(len(nums)):
            result ^= i ^ nums[i]

        return result