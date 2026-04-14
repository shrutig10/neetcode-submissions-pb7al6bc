class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # implement a hash map that store numbers we've seen (key) along with their index (val)
        # iterate through array, checking if the target - cur number is in the hashmap
        # if it is, return [dictionary index, cur index]
        # if not, simply add the number to the dictionary

        seen = {}

        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            else:
                seen[nums[i]] = i
        