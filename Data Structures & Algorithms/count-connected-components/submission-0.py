class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create the adjacency list
        adjList = defaultdict(list)

        # Build the adjacency list
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        # Will track the total components
        # we found
        totalComponents = 0

        # Creating a set to mark nodes as visited
        visited = set()

        # Create our DFS function
        def DFS(node):
            # Skip the node if it's marked
            # as visited
            if node in visited:
                return

            # Mark it as visited
            visited.add(node)

            # Explore all connected neighbors
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    DFS(neighbor)

        # Explore all nodes
        for node in range(n):
            if node not in visited:
                # We found a new component
                totalComponents += 1
                DFS(node)

        # Returning how many components there are
        return totalComponents