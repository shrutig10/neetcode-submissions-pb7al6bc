class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # keep track of longest consecutive
        # keep track of current consectuive count
        # when we see a 1, increment current
        # when we see a 0, compare longest total with cur
        # when we see a 0, set current to 0

        # at the end of the loop compare one more time <- return that

        longest = 0
        cur = 0

        for num in nums:
            if num == 1:
                cur += 1
            else:
                longest = max(longest, cur)
                cur = 0
        
        return max(longest, cur)
        