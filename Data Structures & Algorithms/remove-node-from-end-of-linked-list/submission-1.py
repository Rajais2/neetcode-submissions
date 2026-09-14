# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Creating a dummy node
        dummyNode = ListNode()
        dummyNode.next = head

        # Initialize our slow and fast pointers
        slow, fast = dummyNode, dummyNode

        # Move the fast pointer up to n times
        for i in range(n):
            fast = fast.next

        # Now execute the fast and slow pointer algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        # Now, our slow pointer is at the node before
        # the one we want to remove
        slow.next = slow.next.next

        # Return the new list
        return dummyNode.next