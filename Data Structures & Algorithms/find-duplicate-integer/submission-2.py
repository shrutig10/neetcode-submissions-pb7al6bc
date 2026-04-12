class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use the fact that we are given 1...n+1 as values
        # if we encounter an element that is already negative, then we know that is the duplicate (index)

        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            else:
                nums[(abs(nums[i])) - 1] *= -1
        
        