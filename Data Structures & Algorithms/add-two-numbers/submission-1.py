# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Setting up our dummy node and necessary pointer
        dummyNode = ListNode(0)
        current = dummyNode

        # Setting up for any carries
        carry = 0

        # Keep performing arthimetic until we exhausted
        # everything
        while l1 or l2 or carry:
            # Storing l1's value accordingly
            if l1 is None:
                l1Val = 0
            else:
                l1Val = l1.val
                l1 = l1.next

            # Storing l2's value accordingly
            if l2 is None:
                l2Val = 0
            else:
                l2Val = l2.val
                l2 = l2.next

            # Calculating our total
            total = l1Val + l2Val + carry

            # Extracting the digit and carry
            digit = total % 10
            carry = total // 10

            # Creating our new node and doing updates
            newNode = ListNode(digit, None)
            current.next = newNode
            current = newNode

        # Return our resulting output
        return dummyNode.next