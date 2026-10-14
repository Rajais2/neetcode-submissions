# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a dummy node for our resulting linked list
        dummyNode = ListNode()
        tail = dummyNode

        # Create our priority queue
        PQ = []

        # Loop through the lists to add nodes to our PQ
        for i, node in enumerate(lists):
            if node is not None:
                # Add the node to our PQ
                heapq.heappush(PQ, (node.val, i, node))

        # Repeatedly remove smallest nodes from the
        # PQ until it's empty
        while PQ:
            curNodeVal, position, curNode = heapq.heappop(PQ)

            # Append the node and advance forward
            tail.next = curNode
            tail = curNode

            # Add the successor node if it exists
            if curNode.next is not None:
                heapq.heappush(PQ, (curNode.next.val, position, curNode.next))

        # Return the final ultimate list
        return dummyNode.next