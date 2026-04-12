class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []

        forwards = [1] * len(nums)

        for i in range(1, len(forwards)):
            forwards[i] = forwards[i - 1] * nums[i - 1]
        
        backwards = [1] * len(nums)

        for i in range(len(forwards) - 2, -1, -1):
            backwards[i] = backwards[i + 1] * nums[i + 1]

        for i in range(len(forwards)):
            res.append(forwards[i] * backwards[i])

        return res



        