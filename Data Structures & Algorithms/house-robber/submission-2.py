class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob this house or skip it
        # if we rob this house --> have to skip the next
        # don't rob this house --> option to rob the house
        # most amount of money = max(rob, not rob)
        # rob = this house + rob(skipping the next house)
        # not robbing = max(robbing next house, skipping the next house)

        # dp bottom up solution
        # max money at the last indices = values at those indices
        # otherwise max money = max(this value + dp[i + 2], dp[i + 1])
        # O(1) --> O(n)

        for i in range(len(nums) - 1, -1, -1):
            second = 0 if i + 2 >= len(nums) else nums[i + 2]
            first = 0 if i + 1 >= len(nums) else nums[i + 1]
            nums[i] = max(nums[i] + second, first)

        return nums[0]
        