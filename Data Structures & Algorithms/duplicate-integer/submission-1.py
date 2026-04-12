class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # need to keep track of numbers we've seen
        # set 
        # go through nums
        # if the number is not in the set, add it to the set
        # if the number is in the set, return true

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
        