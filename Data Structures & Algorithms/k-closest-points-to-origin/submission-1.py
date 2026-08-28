class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Creating our heap
        heap = []
        
        # Traversing through each list of points
        for point in points:
            # Storing the x and y coordinates
            x = point[0]
            y = point[1]

            # Getting the point's distance from the origin
            distFromOrigin = (x ** 2) + (y ** 2)

            # Pushing the distance from the origin to the heap
            heapq.heappush(heap, (-distFromOrigin, point))

            # Pop if the size of our heap is bigger than k
            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for element in heap:
            result.append(element[1])

        return result

