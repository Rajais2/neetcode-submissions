"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Creating a dictionary to store 
        # relationships between the cloned nodes
        # and their original counterparts
        clones = {}

        # Creating our DFS recursive function
        def DFS(node):
            # Stop if the node doesn't exist
            if node is None:
                return None

            if node in clones:
                return clones[node]

            # Create a clone and add it to our dict
            clone = Node(node.val)
            clones[node] = clone

            # Explore other neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(DFS(neighbor))

            return clone

        # Return our result from DFSing
        return DFS(node)
