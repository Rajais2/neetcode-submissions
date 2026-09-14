# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Creating a slow and fast pointer
        slow = head
        fast = head

        # Traversing each node
        while fast is not None and fast.next is not None:
            # Moving the slow and fast pointers
            slow = slow.next
            fast = fast.next.next

            # If our pointers overlap, then we have a cycle
            if slow == fast:
                return True

        # Otherwise, we don't
        return False