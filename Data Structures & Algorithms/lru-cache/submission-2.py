# Creating a node class
class Node:
    def __init__(self, key, val):
        # Store the key and val
        self.key = key
        self.val = val
        
        # Default the neighbors to None
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # Initializing necesssary information
        self.capacity = capacity
        self.nodeMap = {}

        # Create our left and right sentiel nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Update their pointesr
        self.left.next = self.right
        self.right.prev = self.left

    # Creating a helper function to remove a node
    def removeNode(self, node):
        # Update necessary pointers
        node.prev.next = node.next
        node.next.prev = node.prev

        # Clear the target node's pointers
        node.next = None
        node.prev = None

    # Creating a helper function to add a node
    def addNode(self, node):
        # Get the previous node
        prevNode = self.right.prev

        # Connect the new node to its neighbors
        node.next = self.right
        node.prev = self.right.prev

        # Update the neighbors to point to the new node
        prevNode.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        # Checking if the key exists
        if key not in self.nodeMap:
            return -1

        # Get the target node
        targetNode = self.nodeMap[key]

        # Update it so it was recently used
        self.removeNode(targetNode)
        self.addNode(targetNode)

        # Return the target node's value
        return targetNode.val

    def put(self, key: int, value: int) -> None:
        # Checking to see if our key already exists
        if key in self.nodeMap:
            # Extract the target node and update it
            targetNode = self.nodeMap[key]
            targetNode.val = value

            # Update it so it was recently used
            self.removeNode(targetNode)
            self.addNode(targetNode)

            # Stop
            return
        
        # Create the new node
        newNode = Node(key, value)

        # Add to both our dictionary and doubly linked list
        self.nodeMap[key] = newNode
        self.addNode(newNode)

        # Checking if we have exceeded max capacity
        if len(self.nodeMap) > self.capacity:
            # Get the node to be deleted
            lruNode = self.left.next

            # Remove it from the linked list
            self.removeNode(lruNode)

            # Remove it from the dictionary
            del self.nodeMap[lruNode.key]
