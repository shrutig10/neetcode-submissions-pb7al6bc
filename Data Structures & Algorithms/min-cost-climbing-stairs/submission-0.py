class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # store the minimum cost at every step
        # work our way down
        # dp bottom up
        # an array that stores minimum cost at a current step
        # work my way backwards
        # the cost at this step is min(dp[i + 1], dp[i + 2])
        # initialize last two indices with current cost (cost[i])
        # return the minimum(dp[0], dp[1])

        dp = [0] * len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            dp[i] = min(dp[i + 1], dp[i + 2]) + cost[i]
        
        return min(dp[0], dp[1])

        