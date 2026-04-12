class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # binary search
        # normally every even index has a new number
        # after the single, every odd index has a new number
        # have a left, right pointer
        # check middle index
        # if no neighbor matches --> is singular element
        # if even index and matches element to the right --> check thr right subarray, otherwise left
        # if odd index and matches element to the left --> check the right subarray, otherwise left


        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if (mid - 1 >= 0 and mid + 1 < len(nums) and nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]) or r - l == 0:
                print('return')
                return nums[mid]
            elif mid % 2 == 0:
                if mid + 1 < len(nums) and nums[mid + 1] == nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        if l < 0:
            return nums[0]
        else:
            return nums[-1]

