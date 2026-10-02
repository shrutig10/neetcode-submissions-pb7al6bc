class Solution:
    def rob(self, nums: List[int]) -> int:
        # at every house you have two options
        # rob this house and skip the next one
        # skip this one
        # keep track of the most amount of money you can make at each house
        # max(nums[i] + rob(nums[i + 2]), rob(nums[i + 1]))
        # save the answers in an array to avoid recalculating
        # to handle the circular case, calcualte without the first house and then without the second house
        # take the max of the two

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        without_first = [0] * (len(nums) - 1)
        without_first[0] = nums[1]
        without_first[1] = max(nums[1], nums[2])

        without_last = [0] * (len(nums) - 1)
        without_last[0] = nums[0]
        without_last[1] = max(nums[0], nums[1])

        for i in range(2, len(without_first)):
            without_first[i] = max(without_first[i - 2] + nums[i + 1], without_first[i - 1])

        for i in range(2, len(without_last)):
                without_last[i] = max(without_last[i - 2] + nums[i], without_last[i - 1])

        return max(without_first[-1], without_last[-1])
