class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # First, we have to sort the list to
        # use the two pointer techinque
        nums.sort()

        # Creating a final container to hold the final results
        result = []

        # Traverse the entire the list
        for i in range(len(nums)):
            # Skipping any duplicates we encounter
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Initializing our two pointers
            left, right = i + 1, len(nums) - 1

            # Performing the two pointer approach
            while left < right:
                # Calculating the sum from all of our pointers
                total = nums[i] + nums[left] + nums[right]

                # Record the triplet if our sum is zero
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Adjust pointers as needed
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    # Depending on our sum value, we have to
                    # move the corresponding pointer
                    if total < 0:
                        left += 1
                    elif total > 0:
                        right -= 1

        # Returning the final list containing all
        # triplets
        return result

        