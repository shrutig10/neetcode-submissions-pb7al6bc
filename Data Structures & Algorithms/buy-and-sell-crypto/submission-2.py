class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # running highest profit seen
        # store the minimum value seen so far
        # iterate through the array
        # saw smaller value than minimum, we can set the minmum to that
        # when we see a val higher than min, calculate profit, compare highest profit we've

        highest = 0
        minimum = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                highest = max(highest, prices[i] - minimum)

        return highest
        