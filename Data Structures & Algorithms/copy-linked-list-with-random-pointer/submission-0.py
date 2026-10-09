"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Resolving a base case
        if head is None:
            return None

        # Create a dictionary to map nodes to their copies
        oldToCopy = {}

        # Create a current pointer to traverse the list
        current = head

        # Traverse the list to fill our dictionary
        while current is not None:
            # Copy the node over and add it our dictionary
            copied_node = Node(current.val)
            oldToCopy[current] = copied_node

            # Move our current pointer to the next node
            current = current.next

        # Begin our second pass to do the deep copying
        current = head

        while current is not None:
            # Set the copied node's next pointer accordingly
            oldToCopy[current].next = oldToCopy[current.next] if current.next else None

            # Set the copied node's random pointer accordingly
            oldToCopy[current].random = oldToCopy[current.random] if current.random else None

            # Move our current pointer to the next node
            current = current.next

        # Return the newly deep copied list
        return oldToCopy[head]