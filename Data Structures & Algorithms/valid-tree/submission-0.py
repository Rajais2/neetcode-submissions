class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If the graph doesn't contain n - 1
        # edges, then there is a cycle somewhere
        if len(edges) != n - 1:
            return False

        # Set up for an adjacency list
        adjList = defaultdict(list)

        # Go through each node and add what
        # nodes they're connected to
        for node, edge in edges:
            adjList[node].append(edge)
            adjList[edge].append(node)

        # Creating a set to track which
        # nodes are fully explored
        visited = set()

        # Creating our DFS recursive function
        def DFS(node):
            # Mark the node as visited
            visited.add(node)

            # Explore all neighbors we haven't encountered
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    DFS(neighbor)

        # Call our DFS recursive function
        DFS(0)

        # Checking if we reach all nodes, which
        # determines if it is a tree or not
        if len(visited) == n:
            return True
        else:
            return False