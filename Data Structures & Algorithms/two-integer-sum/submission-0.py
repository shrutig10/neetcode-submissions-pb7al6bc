class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force: try every single combination and see if it adds to target
        # keep track of what we've seen
        # if we need that number (that we have previously seen), then valid solution
        # we have to return indices, so keep track of the value and the index
        # create a dictionary that stores val --> index

        seen = dict()

        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            if num not in seen:
                seen[num] = i
        