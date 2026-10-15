class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Will help with movements
        k = 0

        # Begin list traversal!!!!!!!!!!!!
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k