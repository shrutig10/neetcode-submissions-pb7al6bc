class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use binary search
        # using l, mid, r
        # two of these will always be in the same sorted segment
        # if mid > r, then eliminate l by changing l to mid + 1
        # if mid < r, then eliminate r by changing r to mid 
        # if l and r are the same, return that element


        l, r = 0, len(nums) - 1

        while l != r:
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]



        