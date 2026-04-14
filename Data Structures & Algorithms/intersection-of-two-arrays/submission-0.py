class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # make one list into a set --> O(1) lookup time
        # iterate through the other array (with duplicates taken out) and see if its values are in the first set
        # add to an array

        set1 = set(nums1)
        list2 = list(set(nums2))
        res = []

        for num in list2:
            if num in set1:
                res.append(num)

        return res