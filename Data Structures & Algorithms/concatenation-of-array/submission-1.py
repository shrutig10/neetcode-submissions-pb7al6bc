class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # create a copy of nums
        # append nums to it?
        # return nums + nums

        # alternate solution
        # create new array twice the size
        # keep another index that starts at n
        # incrememnt both at the same time and copy to new array

        k = len(nums)
        res = [0] * 2 * len(nums)
        for i in range(len(nums)):
            res[i] = res[k] = nums[i]
            k += 1

        return res