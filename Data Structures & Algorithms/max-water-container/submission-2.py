class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # calculate water = (minimum height of two bars) * distance between two bars
        # two pointers - left and right edges
        # calculate area there
        # if left is smaller or l/r are equal -> move left one forward
        # if the right is smaller -> move right backwards
        # keep trying until l = r --> area = 0
        # keep a running maximum and compare with calculated area

        maximum = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maximum = max(maximum, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maximum