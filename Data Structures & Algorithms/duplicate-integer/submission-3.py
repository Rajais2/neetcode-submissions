class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Making an empty set to store previously seen numbers
        seen = set()

        # Looping through each number in our list
        for num in nums:
            # If we have already seen this number, it is a duplicate
            if num in seen:
                return True
            else:
                # Otherwise, we add it to the set
                seen.add(num)

        # If we have traversed the whole list, there are
        # no duplicates present
        return False




        