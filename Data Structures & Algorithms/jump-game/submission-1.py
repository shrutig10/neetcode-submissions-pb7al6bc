class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # when you hit 0, you're stuck
        # backtracking
        # try to go maximum, if you hit a 0, then backtrack and try 1 less

        # base case: idx == last index, return true
        # at a 0 --> return false
        # loop from the current jump value to 1, if you can make it to the end, return true

        def jump(idx):
            if idx >= len(nums) - 1:
                return True
            if nums[idx] == 0:
                return False

            for i in range(nums[idx], 0, -1):
                if jump(idx + i):
                    return True

            return False

        return jump(0)
        