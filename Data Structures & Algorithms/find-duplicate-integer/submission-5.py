class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Setting up our slow and fast pointers
        slow = nums[0]
        fast = nums[0]

        # Essentially doing a do-while loop
        while True:
            # Advancing our pointers
            slow = nums[slow]
            fast = nums[nums[fast]]

            # Exit if we're at the same point
            if slow == fast:
                break

        # Resetting our slow pointer to the beginning
        slow = nums[0]

        # Keep moving until pointers collide
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # Either pointer is at the duplicate number
        return slow
        