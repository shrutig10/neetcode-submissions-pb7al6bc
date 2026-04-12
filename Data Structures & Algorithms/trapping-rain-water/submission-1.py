class Solution:
    def trap(self, height: List[int]) -> int:
        # want to keep track of the max height of the wall from both the left and right
        # when calculating the water at a particular index, we want to limit to the 
        # minimum wall between the maximum lefts and rights
        # subtract that amount by the wall at that index
        # have a l and r pointer 
        # store a max left and max right (wall height)
        # maxHeight - curHeight = water that can be trapped 
        # adjust max left or max right accordingly at the end
        # stop when l and r are at the same place

        total = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(height[l], maxL)
                total += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                total += maxR - height[r]

        return total

        