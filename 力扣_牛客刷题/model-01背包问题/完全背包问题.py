class Solution:
    def change(self, amount, coins):
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp


s = Solution()
s.change(amount=5, coins=[1, 2, 5])
