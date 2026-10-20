class Solution:   
    def sortArray(self, nums: List[int]) -> List[int]:
        # Checking if our initial list is empty
        if not nums:
            return []
        
        # Creating a helper function to perform 
        # merge sort
        def mergeSort(arr):
            # Check for base case
            if len(arr) == 1:
                return arr
            
            # Calculate the middle position
            mid = len(arr) // 2

            # Extract the two halves
            leftSide = arr[0:mid]
            rightSide = arr[mid:]

            # Sorts both sides
            leftSorted = mergeSort(leftSide)
            rightSorted = mergeSort(rightSide)

            # Creating incremental variables
            i = 0
            j = 0

            # Creating our final list
            result = []

            # Now begin the merge
            while i < len(leftSorted) and j < len(rightSorted):
                # Add the smaller element
                if leftSorted[i] <= rightSorted[j]:
                    result.append(leftSorted[i])
                    i += 1
                elif rightSorted[j] < leftSorted[i]:
                    result.append(rightSorted[j])
                    j += 1

            # Add any leftovers
            result += leftSorted[i:]
            result += rightSorted[j:]

            # Return the final result
            return result

        # Call the function on the initial list
        return mergeSort(nums)