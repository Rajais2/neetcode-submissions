class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Create an adjacency list
        adjList = defaultdict(list)

        # Creating a DFS recursive function to check
        # if we can reach a target node from one
        # node
        def DFS(node, target, visited_path):
            # We have reached that node
            if node == target:
                return True

            # If we explored the same node, then
            # that path does us no good
            if node in visited_path:
                return False

            # Mark the node as visited
            visited_path.add(node)

            # Explore all neighbors seeing if they 
            # can reach the target
            for neighbor in adjList[node]:
                if DFS(neighbor, target, visited_path):
                    return True

            # Otherwise, we can't reach the
            # target
            return False

        # Traverse through each edge
        for u, v in edges:
            # Create a fresh visited set for
            # each edge
            visited = set()

            # If u and v are already connected, adding
            # another edge will cause a cycle
            if DFS(u, v, visited):
                return [u, v]
            else:
                # Otherwise, add the edge to our
                # adjacency list
                adjList[u].append(v)
                adjList[v].append(u)