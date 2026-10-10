class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create an adjacency list
        adjList = defaultdict(list)

        # Build our adjacency list
        # This is a directed and weighted graph
        for source, dest, weight in times:
            adjList[source].append((dest, weight))

        # Initialize all node distances (labeled 1 to n)
        nodeDists = {node: float('inf') for node in range(1, n + 1)}

        # Update our starting node's distance
        nodeDists[k] = 0

        # Create our priority queue and add our start node
        priorityQueue = []
        heapq.heappush(priorityQueue, (0, k))

        # Perform dijkstra's algoritm
        while priorityQueue:
            # Extract our current node and its distance
            curDist, curNode = heapq.heappop(priorityQueue)

            # Skip this distance if it's worst
            if curDist > nodeDists[curNode]:
                continue

            # Update the distance if it's better
            nodeDists[curNode] = curDist

            # Explore the current node's neighbors
            for dest, weight in adjList[curNode]:
                # Get the new distance
                newDist = curDist + weight

                # Update the distance if it's better
                # and add the node to the PQ
                if nodeDists[dest] > newDist:
                    nodeDists[dest] = newDist
                    heapq.heappush(priorityQueue, (nodeDists[dest], dest))

        # Checking if it's impossible for the signal
        # to reach all nodes
        if any(dist == float('inf') for dist in nodeDists.values()):
            return -1

        # Otherwise, just return the largest shortest-path
        return max(nodeDists.values())