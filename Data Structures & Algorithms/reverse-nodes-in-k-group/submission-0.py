
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create a dummy node for the final list
        dummyNode = ListNode()
        dummyNode.next = head

        # Create a position pointer to track the node
        # immediately before the group we're currently
        # processing
        position = dummyNode

        # Keep processing groups
        while True:
            # Create a temp pointer to check if we have k
            # nodes left
            kthNode = position

            # Attempt to advance k nodes
            for i in range(k):
                kthNode = kthNode.next

                # Stop if there aren't enough nodes remaining
                if kthNode is None:
                    return dummyNode.next

            # Save the node immediately after the current group
            groupNext = kthNode.next

            # Save the original first node of the group
            groupStart = position.next

            # Set up pointers for the reversal process
            cur = groupStart
            prev = groupNext

            # Reverse up to k nodes
            for i in range(k):
                nextNode = cur.next
                cur.next = prev
                prev = cur
                cur = nextNode

            # Reconnect the reversed group
            position.next = prev

            # Advance position to the tail of the reversed group
            position = groupStart