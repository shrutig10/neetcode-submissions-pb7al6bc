class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force: for every number, multiply all other numbers and add it to the result
        # run in O(n^2) time 
        # doing a lot of the same calculations again
        # want an array that stores previous calculations
        # can have an array that stores the product of all elements before the current element
        # have another array that stores the product of all elements after the current element
        # when creating final array, multiple before product with after product
        # if there are not elements before/after the array, then write 1

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        res = []

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res


        
