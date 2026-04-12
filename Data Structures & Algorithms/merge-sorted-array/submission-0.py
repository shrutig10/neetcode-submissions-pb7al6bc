class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # could shift all elements of num1 down if nums2 < nums1
        # no shifting: went backwards
        # iterate through ENTIRE nums1 backwards
        # have a pointer for end of nums1 and nums2
        # whichever one is greater --> placed at where I am in nums1 (entire list)
        # check that either nums1 or nums2 pointer is not less than 0

        l1, l2 = m - 1, n - 1

        for i in range(len(nums1) - 1, -1, -1):
            if l2 < 0:
                nums1[i] = nums1[l1]
                l1 -=1 
            elif l1 < 0:
                nums1[i] = nums2[l2]
                l2 -= 1
            else:
                if nums1[l1] > nums2[l2]:
                    nums1[i] = nums1[l1]
                    l1 -= 1
                else:
                    nums1[i] = nums2[l2]
                    l2 -= 1

                
        