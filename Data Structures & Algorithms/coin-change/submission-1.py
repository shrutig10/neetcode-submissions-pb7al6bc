class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # recursive problem to try out different paths
        # base case: amount is 0, return 0 coins
        # try the current coin, and then while it is <= amount left, we can keep using that coin
        # once we can use that coin anymore, move on to the next coin
        # min(1 + dfs(amount - coins[i])) <- if we chose to use this coin
        # an array that stores the minimum coins we need to make the amount
        # this array would be as many elements as amount
        # initialize as total amount
        # left to right through this array
        # loop through coins and see what the minimum amount to build that amount is 
        # store that in the array and keep going
        # once we try a coin, we would check the array for dp[amount - coin[i]] + 1 would make this amount
        # return dp[amount]

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                curAmount = i
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] > amount else dp[amount]

            

        