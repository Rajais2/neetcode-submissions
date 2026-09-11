class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Creating a dictionary to store frequencies
        frequencies = {}

        # Creating our minimum heap
        minHeap = []

        # Going through each number to store their
        # frequencies
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        # Going through our dictionary to store the
        # top k frequent items
        for key, value in frequencies.items():
            # Push the dictionary item to our heap
            heapq.heappush(minHeap, (value, key))

            # If our min heap exceeds our k, simply
            # pop it
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [key for value, key in minHeap]

            

