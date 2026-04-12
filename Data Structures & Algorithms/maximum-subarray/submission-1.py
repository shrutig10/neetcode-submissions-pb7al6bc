class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # two pointers: left pointer and a right pointer
        # increment the right pointer and calculate sum by adding the right element to the cur sum
        # once the right pointer reaches the end, then start moving the left pointer and subtracting from the cur sum
        # continusouly look for the maximum between the current stored max and the cur sum
        # condition for the loop will be the left < right and right pointer needs to be < len of the lsit

        cur_sum = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > cur_sum + nums[i]:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            maximum = max(cur_sum, maximum)

        return maximum

