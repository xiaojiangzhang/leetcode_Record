'''
给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个
属性。其中第 i 个物品的重量为 wt[i]，价值为 val[i]，现在让你用这个
背包装物品，最多能装的价值是多少？
'''


# 定义状态dp[i][j]表示前i个物品，重量为j时可装的最大价值为dp[i][j]

class Solution():
    def knaknapsack01_ADM(self, w, v, c):
        n = len(w)
        dp = [[0 for _ in range(c + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, c + 1):
                if c - w[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])

        return dp


s = Solution()
re = s.knaknapsack01_ADM([1, 2, 3], [6, 10, 12], 5)
print(re)
