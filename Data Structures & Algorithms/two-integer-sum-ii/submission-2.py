class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Setting up a two pointer approach
        left, right = 0, len(numbers) - 1

        # Keep performing operations until our pointers overlap
        while left < right:
            # Get the current sum from our two values
            curSum = numbers[left] + numbers[right]

            # If our current sum is the target, we
            # return the pointer indices (one indexed)
            if curSum == target:
                return [left + 1, right + 1]
            elif curSum > target:
                # If our current sum is more than 
                # the target, we need smaller numbers
                right -= 1
            elif curSum < target:
                # If our current sum is less than
                # the target, we need bigger numbers
                left += 1
        
        # Return an empty list if we traversed
        # the entire list
        return []