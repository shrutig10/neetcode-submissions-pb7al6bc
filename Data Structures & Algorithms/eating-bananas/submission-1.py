import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # upper bound for k is the max value in piles
        # lower bound for k is 1 (if h = sum of all vals in piles)

        # get the k
        # how to test --> each pile takes ceil(x / k) hours to eat
        # use a binary search to test different values of k
        # if within hours, then try less --> store this in a minimum
        # if over hours, try more

        min_speed = max(piles)
        l, r = 1, min_speed

        while l <= r:
            mid = l + (r - l) // 2
            test_hours = 0

            for pile in piles:
                test_hours += math.ceil(pile / mid)
            
            if test_hours <= h:
                r = mid - 1
                min_speed = min(min_speed, mid)
            else:
                l = mid + 1

        return min_speed




        