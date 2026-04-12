class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # keep track of running highest sum
        # iterate through my array
        # keep a current sum 
        # does adding this element help me? 
        # does adding this number result in a sum that is > or < this number itself
        # take the max at each iteration

        highest = cur = nums[0]

        for i in range(1, len(nums)):
            if cur + nums[i] < nums[i]:
                cur = nums[i]
            else:
                cur += nums[i]
            
            highest = max(highest, cur)

        return highest
        