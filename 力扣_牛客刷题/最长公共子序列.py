"""
给定字符串s1和字符串s2，返回这两个字符串的最长公告子序列
s1 = ABCG
s2 = ASCBHDCHG
最长公共字符串序列长度为4
"""

"""
问题描述：
求解LCS（m,n），其中m代表s1[0...m],n代表s2[0...n]的最长公共子序列的长度
情况一：
s1[m] == s2[n]:
LCS(m, n) = 1 + LCS(m - 1, n - 1)
情况二：
s1[m] != s2[n]:
LCS(m, n) = max(LCS(m - 1, n), LCS(m, n - 1))
"""


class Solution:
    # 递归加记忆搜索求解
    def get_MAX_subLength(self, s1, s2):
        m = len(s1)
        n = len(s2)
        self.memo = [[0 for _ in range(n)] for _ in range(m)]
        if m == 0 or n == 0:
            return 0
        return self.LCS(s1, s2, m - 1, n - 1)

    def LCS(self, s1, s2, m, n):
        if m == -1 or n == -1:
            return 0
        if self.memo[m][n] != 0:
            return self.memo[m][n]
        if s1[m] == s2[n]:
            res = 1 + self.LCS(s1, s2, m - 1, n - 1)
            self.memo[m][n] = res
            return res
        else:
            r = max([self.LCS(s1, s2, m - 1, n), self.LCS(s1, s2, m, n - 1)])
            self.memo[m][n] = r
            return r

    def dp_LCS(self, s1, s2):
        m, n = len(s1), len(s2)
        memo = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max([memo[i][j - 1], memo[i - 1][j]])
        return memo[-1][-1]

    def dp(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max([dp[i - 1][j], dp[i][j - 1]])
        return dp[-1][-1]


s1 = "abcde"
s2 = "ace"
s = Solution()
res = s.dp(s1, s2)
print(res)
