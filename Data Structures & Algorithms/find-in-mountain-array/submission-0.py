class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # binary search
        # split array into two sorted pieces
        # one is increasing, one is decreasing
        # find the mountain (peak) <-- is this the target?
        # search the left side of the mountain for the target
        # search the right of the mountain for the target
        # conditions for finding the mountain
        # if arr[i - 1] < arr[i] < arr[i + 1], move left
        # otherwise if > >, move the right
        # else we must be at the peak <-- break (mid is peak)
        # left side --> classic binary search
        # right side --> swap cases for left and right pointer to move

        # step 1: find peak
        length = mountainArr.length()
        l, r = 1, length - 2

        while l <= r:
            mid = (l + r) // 2
            leftEl = mountainArr.get(mid - 1)
            curEl = mountainArr.get(mid)
            rightEl = mountainArr.get(mid + 1)

            if leftEl < curEl < rightEl:
                l = mid + 1
            elif leftEl > curEl > rightEl:
                r = mid - 1
            else:
                break

        peak = (l + r) // 2
        
        if mountainArr.get(peak) == target:
            return peak

        # bin search on left side
        l, r = 0, peak - 1

        while l <= r:
            mid = (l + r) // 2
            curEl = mountainArr.get(mid)

            if curEl < target:
                l = mid + 1
            elif curEl > target:
                r = mid - 1
            else:
                return mid

        # bin search on the right side
        l, r = peak + 1, length - 1

        while l <= r:
            mid = (l + r) // 2
            curEl = mountainArr.get(mid)

            if curEl > target:
                l = mid + 1
            elif curEl < target:
                r = mid - 1
            else:
                return mid

        return -1





