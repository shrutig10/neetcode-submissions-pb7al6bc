class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up dp solution
        # store an array with solutions to problem
        # go backwards from n to 0 and fill in array
        # for n and n - 1, the value can be 1
        # otherwise, the value will be dp[i + 1] + dp[i + 2]
        # dp[0]

        dp = [0] * (n + 1)
        dp[n] = 1
        dp[n - 1] = 1

        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]