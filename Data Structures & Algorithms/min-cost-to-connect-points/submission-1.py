class Solution:
    # Create a find() function for union-find
    def find(self, parents, x):
        while parents[x] != x:
            x = parents[x]
            
        return x
    
    # Create an union() function for union-find
    def union(self, x, y, parents):
        # Find the roots of x and y
        x = self.find(parents, x)
        y = self.find(parents, y)

        # Stop if they are already connected, otherwise
        # make one the parent of the other
        if x == y:
            return False
        else:
            parents[y] = x

        return True
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Creating a list to hold the costs for
        # all edges
        edgeInfo = []

        # Calculate the cost for each edge and
        # add it our overall list
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                # Calculate the cost
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                # Add to our list (the coordiantes and their cost)
                edgeInfo.append((cost, i, j))

        # Sort the edges ascending based on their weights
        sorted_edges = sorted(edgeInfo, key = lambda edge : edge[0])

        # Create a parent list for union-find
        parent = list(range(len(points)))

        # Create a total cost and edge counter
        total = 0
        edgeCounter = 0

        # Go through our edges and find the minimum cost
        for cost, x, y in sorted_edges:
            # Add the cost if the edge is valid
            if self.union(x, y, parent) == True:
                total += cost
                edgeCounter += 1

            if edgeCounter == len(points) - 1:
                break

        # Return the total minimum cost
        return total