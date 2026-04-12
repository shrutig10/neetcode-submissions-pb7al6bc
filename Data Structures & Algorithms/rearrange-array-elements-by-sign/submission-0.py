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

        res = []

        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])

        return res