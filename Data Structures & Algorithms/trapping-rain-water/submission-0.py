class Solution:
    def trap(self, height: List[int]) -> int:
        # keep track of the max left and max right
        # take the minimum of these values and subtract current height to get the water amount
        # keep an array that stores the current max left and an array that stores current max right
        # array is an O(n) space solution, we want O(1)
        # keep a left and right pointer that stores current max of left and right we've seen
        # take the min of those
        # when r > l, shift the right over 
        # if leftMax <= rightMax, process left side
        # process right side
        # running water count

        total = 0

        l, r = 0, len(height) - 1
        leftMax = rightMax = 0

        while l <= r:
            boundary = min(leftMax, rightMax)
            if leftMax <= rightMax:
                total += max(0, boundary - height[l]) 
                leftMax = max(height[l], leftMax)
                l += 1
            else:
                total += max(0, boundary - height[r])
                rightMax = max(height[r], rightMax)
                r -= 1

        return total

