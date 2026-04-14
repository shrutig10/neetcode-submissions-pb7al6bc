class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # go through the array and keep in another array the unique numbers
        # iterate through the array again, changing the first k elements as needed
        # this is not an in place solution as we are creating another array (O(n) space)

        # could try to swap numbers
        # have a pointer that points to the next position where unique will be placed
        # as you iterate through the array, when you find a unique number, you place it at the 
        # old pointer and move that old pointer
        # store prev or can do nums[l - 1] to get prev number

        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[l - 1]:
                nums[l] = nums[r]
                l += 1

        return l
