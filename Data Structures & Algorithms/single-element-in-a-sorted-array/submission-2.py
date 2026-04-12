class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # do a binary search
        # correct pattern: new num starts on even indices and old nums on odd indices
        # if our current num is at an even index and does not match number to the right, order
        # got off on the left subarray (r = mid)
        # else got off on right subarray (l = mid + 1)
        # if our current num is at an odd index and does not match number to the left, order got off on 
        # the left (r = mid)
        # else off on right subarray (l = mid + 1)
        # while l < r

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if (mid % 2 == 0 and nums[mid] != nums[mid + 1]) or (mid % 2 == 1 and nums[mid] != nums[mid - 1]):
                r = mid
            else:
                l = mid + 1
        
        return nums[(l + r) // 2]
            
        