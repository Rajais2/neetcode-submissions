class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initializing our parameters
        self.minHeap = []
        self.k = k

        # Traverse through all of our numbers
        for num in nums:
            # Push the number onto our min heap
            heapq.heappush(self.minHeap, num)

            # If our heap is bigger than our k, pop it
            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Push the number onto our min heap
        heapq.heappush(self.minHeap, val)

        # If our heap is bigger than our k, pop it
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Return the kth largest integer in the stream
        return self.minHeap[0]
        
