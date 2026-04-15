class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        # peform a binary search on the array
        # include a check after element not found for l == r, if so then return that index

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            else:
                if l == r:
                    if nums[mid] < target:
                        return l + 1
                    else:
                        return l
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

        return l
        
