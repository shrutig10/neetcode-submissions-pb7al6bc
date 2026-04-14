class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # implement a two pointer solution
        # l starting at beg of array
        # r iterates through array
        # if r != val, then copy into l and increment l
        # otherwise skip!

        l = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        
        return l