# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Setting up our two pointers for reversal
        prev = None
        current = head

        # Traversing through all of our nodes
        while current is not None:
            # Saving the current node
            nextNode = current.next

            # Reversing the link
            current.next = prev

            # Advance both pointers forward
            prev = current
            current = nextNode

        # In the end, this will be the new head
        return prev