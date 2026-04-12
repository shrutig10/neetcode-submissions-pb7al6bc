class Solution:
    def mySqrt(self, x: int) -> int:
        # brute force: try every number's square
        # once you get too high, then you take the previous number

        if x < 2:
            return x
        
        for i in range(x):
            prod = i * i
            if prod == x:
                return i
            if prod > x:
                return i - 1

        