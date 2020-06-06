# 给定一个正整数
# n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

class Solution:
    def integerBreak(self, n):
        self.re = [0 for _ in range(n + 1)]
        return self.integerBreak2(n)

    # 递归方法
    def breakIntreger(self, n):
        if n == 1:
            return 1
        result = -1
        for i in range(1, n):
            result = max([result, i * (n - i), i * self.integerBreak(n - i)])
        return result

    # 记忆搜索
    def integerBreak2(self, n):
        if n == 1:
            return 1
        if self.re[n] != 0:
            return self.re[n]
        result = 0
        for i in range(1, n + 1):
            result = max([result, i * (n - i), i * self.integerBreak2(n - i)])
        self.re[n] = result
        return self.re[n]

    # 动态规划
    def integerBreak3(self, n):
        if n == 1:
            return 1
        record = [-1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                record[i] = max([record[i], j * (i - j), j * record[i - j]])
        return record[n]


s = Solution()
print(s.integerBreak(10))
