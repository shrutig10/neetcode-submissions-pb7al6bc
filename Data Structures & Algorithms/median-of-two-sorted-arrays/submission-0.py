class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search
        # median --> equal amounts to the left and to the right 
        # perform a binary search on one of the arrays 
        # x elements to the left of median (n + m / 2)
        # y elements in the array that are part of the left partition
        # x - y elements in the other array will belong to the left partition
        # check validity of left partition --> max of left < min right for both arrays
        # if so, compute median
        # otherwise --> compute a new partition
        # [1, 3] [4, 4] --> [1, 4] [3, 4] --> shift the left pointer to mid + 1, otherwise shift right to mid - 1
        # odd number of elements: take the value after the last element in the left partition
        # even number of elements: max of lefts and min of the rights

        total = len(nums1) + len(nums2)
        partLen = total // 2

        if len(nums1) < len(nums2):
            shorter = nums1
            longer = nums2
        else:
            shorter = nums2
            longer = nums1

        l, r = 0, len(shorter) - 1

        while True:
            mid = (l + r) // 2
            longer_index = partLen - mid - 2

            shorterLeftPart = shorter[mid] if mid >= 0 else float('-inf')
            shorterRightPart = shorter[mid + 1] if mid < len(shorter) - 1 else float('inf')
            longerLeftPart = longer[longer_index] if longer_index >= 0 else float('-inf')
            longerRightPart = longer[longer_index + 1] if longer_index < len(longer) - 1 else float('inf')

            if longerLeftPart <= shorterRightPart and shorterLeftPart <= longerRightPart:
                if total % 2:
                    return float(min(shorterRightPart, longerRightPart))
                else:
                    return (max(shorterLeftPart, longerLeftPart) + min(shorterRightPart, longerRightPart)) / 2
            elif shorterRightPart < longerLeftPart:
                l = mid + 1
            else:
                r = mid - 1

        
        