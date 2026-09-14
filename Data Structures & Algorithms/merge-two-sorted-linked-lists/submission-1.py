# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Creating nodes to simply extract nodes
        # in the future
        dummyNode = ListNode()
        tail = dummyNode

        # Traverse both lists
        while list1 is not None and list2 is not None:
            # Checking if nodes from the first list 
            # has smaller values
            if list1.val <= list2.val:
                # Add the node from the first list
                tail.next = list1
                list1 = list1.next
            else:
                # Otherwise, add the node from the second list
                tail.next = list2
                list2 = list2.next

            # Move the tail to progress through the list
            tail = tail.next

        # Checking if we have any leftover nodes
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        # Returning the new list we built
        return dummyNode.next