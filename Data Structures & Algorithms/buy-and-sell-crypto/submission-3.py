class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # want the smallest possible buy price and the largest possible sell price
        # sell price must come before the buy price
        # sliding window
        # extend our right side (sell price)
        # move the buy date if you find a smaller price
        # must move the sell date if buy and sell are on the same day
        # keep track of largest profit (start at 0)

        profit = 0
        buyPrice = prices[0]
        r = 1

        while r < len(prices):
            curProf = prices[r] - buyPrice
            if curProf > profit:
                profit = curProf
            elif prices[r] < buyPrice:
                buyPrice = prices[r]
            r += 1

        return profit

        