class Solution:
    def rob(self, nums: List[int]) -> int:
        # at every house we can skip or we can rob
        # if we rob, we must skip the next house
        # if we skip, we have the same decision as before (skip/rob) for the next house
        # use dynamic programming to help
        # rob the street from l to r
        # at every house h, the most money you can make is 
        # the most amount of money from house h - 2 + this house's value
        # OR the most amount of money from house h - 1

        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[-1]

        