class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # counting the 0, 1, 2 and then creating a new array with those
        # keep track of if we've seen a 0 or 1, and then when we encounter a 
        # number larger, we can swap
        # we see a 0 but we know we've seen a 1, then we can swap postions

        # kept track of the last seen 0/first seen 1, and then swap elements

        freqs = [0] * 3

        for num in nums:
            freqs[num] += 1

        for i in range(len(nums)):
            if freqs[0]:
                nums[i] = 0
                freqs[0] -= 1
            elif freqs[1]:
                nums[i] = 1
                freqs[1] -= 1
            elif freqs[2]:
                nums[i] = 2
                freqs[2] -= 1

        


        