# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Setting up fast and slow pointers
        fast, slow = head, head

        # Executing the fast and slow pointer tatic
        while fast and fast.next:
            # Advance our pointers
            slow = slow.next
            fast = fast.next.next

        # Now, slow is at the midpoint and we 
        # can take advantage of this
        newHead = slow.next
        slow.next = None
        prev = None

        # Traverse through the second part of the list
        while newHead:
            # Store the next node in sequence
            nextNode = newHead.next

            # Reverse the link
            newHead.next = prev

            prev = newHead
            newHead = nextNode

        # Setting up pointers to traverse both halves now
        l1 = head
        l2 = prev

        # Traverse both lists to begin merging them
        while l1 and l2:
            # Saving the next nodes
            l1nextNode = l1.next
            l2nextNode = l2.next

            # Rewiring the nodes
            l1.next = l2
            l2.next = l1nextNode

            # Advancing our pointers
            l1 = l1nextNode
            l2 = l2nextNode


