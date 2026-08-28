class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We have to negate weights to use a max heap
        for i, stone in enumerate(stones):
            stones[i] = -stone

        # Creating our heap
        heap = []

        # Add all of our negated stones into our heap
        for stone in stones:
            heapq.heappush(heap, stone)

        # Keep performing operations as long as we have
        # two stones
        while len(heap) > 1:
            # Get our two stones
            firstStone = abs(heapq.heappop(heap))
            secondStone = abs(heapq.heappop(heap))

            if secondStone < firstStone:
                heapq.heappush(heap, -(firstStone - secondStone))

        if len(heap) == 0:
            return 0
        else:
            return abs(heap[0])