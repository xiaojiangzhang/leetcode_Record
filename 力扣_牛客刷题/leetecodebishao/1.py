class Solution:
    # 状态天数，题目数,是否由小杨做题dp[i][k][1/0]
    # 转移：dp[i][k][0] = min(dp[i-1][k-1][0],dp[i-1][k-1][1]+w[k])
    # dp[i][k][0]第i天第k题没有做，
    # dp[i][k][0] = dp[i-1][k][0],dp[i-1][k-1][1]+time[k]，dp[i-1][k-1][2]
    # dp[i][k][1] = dp[i-1][k][0],dp[i-1][k-1][1]+time[k], dp[i-1][k-1][2]
    # dp[i][k][2] = dp[i-1][k-1][2]+dp[i-1][k-1][1]+time[k],dp[i-1][k][0]
    def minTime(self, time, m):
        n = len(time)
        if n <= m or len(time) == 0:
            return 0
        dp = [[[float('INF'), float('INF'), float('INF')] for i in range(n + 1)] for _ in range(m)]
        for i in range(m):
            for k in range(1, n + 1):
                if i == 0:
                    dp[i][k][0] = float('INF')
                    dp[i][k][1] = time[i]
                    dp[i][k][2] = 0
                    continue
                dp[i][k][0] = min(dp[i - 1][k][0], dp[i - 1][k - 1][1] + time[k - 1], dp[i - 1][k - 1][2])
                dp[i][k][1] = min(dp[i - 1][k][0], dp[i - 1][k - 1][1] + time[k - 1], dp[i - 1][k - 1][2])
                dp[i][k][2] = min(dp[i - 1][k - 1][2] + dp[i - 1][k - 1][1] + time[k - 1], dp[i - 1][k][0])
        return dp[-1][n - 2][1]


s = Solution()
res = s.minTime([999, 999, 999, 1, 1], m=4)
print(res)
