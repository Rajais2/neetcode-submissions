class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Creating a dict to store individual frequencies
        frequencies = {}

        # Traversing through each number to track each frequency
        for num in nums:
            # If it exists, increment by one
            if num in frequencies:
                frequencies[num] += 1
            else:
                # Otherwise, make it start at 1
                frequencies[num] = 1

        # Sorting the dict based on the frequencies
        # Lambda function: pair[0] -> number, pair[1] -> frequency,
        # reverse is true because we want in descending order (sorted does
        # ascending by default)
        sorted_freq = sorted(frequencies.items(), key = lambda pair: pair[1], reverse = True)

        # Making a final container to hold our final answer
        answer = []

        # Looping for up to k most frequent elements
        for i in range(k):
            # Here, the first index is the number so append that
            answer.append(sorted_freq[i][0])
        
        # Returning the final container
        return answer
