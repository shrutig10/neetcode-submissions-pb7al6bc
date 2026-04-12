class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # 2 sorted arrays
        # do a binary search on both sorted arrays --> time is still logn
        # need to find where the rotation starts/pivot point
        
        # binary search to find the pivot --> minimum
        # is the middle greater than the right pointer? --> middle belongs to the left sorted array
        # if greater, then adjust left pointer to mid + 1
        # if middle less than the right pointer --> belongs to the right sorted array
        # adjust right pointer to mid
        # do this until left and right are the same --> pivot


        # find pivot
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = r

        def bin_search(l, r, nums, target):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
                
            return -1

        res = bin_search(0, pivot - 1, nums, target)

        if res == -1:
            res = bin_search(pivot, len(nums) - 1, nums, target)

        return res
            







        