class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # create a pos and neg array
        # when we see a positive, add to pos array, when we see a neg add to negative
        # build a new array from there

        pos = []
        neg = []

        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        for i in range(0, len(nums) // 2):
            nums[i * 2] = pos[i]
            nums[i * 2 + 1] = neg[i]

        return nums