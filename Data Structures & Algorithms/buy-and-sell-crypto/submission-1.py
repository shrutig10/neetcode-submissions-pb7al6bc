class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy will always be before sell
        # start at 0
        # want to buy for the cheapest and sell for highest profit

        profit = 0
        buy = prices[0]

        for sell in prices:
            if sell - buy > profit:
                profit = sell - buy
            if sell < buy:
                buy = sell

        return profit
        
        