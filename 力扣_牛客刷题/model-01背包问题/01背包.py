class Solution:
    def knapsack01(self, weight, value, c):
        return self.getMax(weight, value, c, len(weight) - 1)

    def getMax(self, w, v, c, index):
        if index < 0 or c <= 0:
            return 0

        # 第一种情况，不考虑当前index指向的物品，直接看index+1物品的价值和重量
        res = self.getMax(w, v, c, index - 1)
        # 第二种情况，直接将当前index指向物品放入背包
        if c >= w[index]:
            res = max([res, v[index] + self.getMax(w, v, c - w[index], index - 1)])
        return res

    def knapsack01_memo(self, weight, value, c):
        self.memo = [[-1 for _ in range(c + 1)] for _ in range(len(weight))]
        return self.getMax_memo(weight, value, c, len(weight) - 1)

    def getMax_memo(self, w, v, c, index):
        if index < 0 or c <= 0:
            return 0
        if self.memo[index][c] is not -1:
            return self.memo[index][c]
        # 第一种情况，不考虑当前index指向的物品，直接看index+1物品的价值和重量
        res = self.getMax_memo(w, v, c, index - 1)
        # 第二种情况，直接将当前index指向物品放入背包
        if c >= w[index]:
            res = max([res, v[index] + self.getMax_memo(w, v, c - w[index], index - 1)])
        self.memo[index][c] = res
        return res

    # dp求解背包问题
    def knapsack01_dp(self, w, v, c):
        memo = [[-1 for _ in range(c + 1)] for _ in range(len(v))]
        for i in range(c + 1):
            memo[0][i] = v[0] if i >= w[0] else 0
        for time in range(1, len(v)):
            for c in range(c + 1):
                # 情况一 直接计算当前容量至少存放的最大价值
                memo[time][c] = memo[time - 1][c]
                if c >= w[time]:
                    memo[time][c] = max([memo[time][c], v[time] + memo[time - 1][c - w[time]]])
        return memo[-1][-1]

    '''优化空间复杂度，在dp实现过程中，我们发现在创建w.size行，c+1列数组时，我们整个过程中只用了两行数组，、
    所以在空间上还有很大的空间可以优化。'''

    def knapsack01_ADM(self, w, v, c):
        memo = [[0 for _ in range(c + 1)] for _ in range(2)]
        for i in range(c + 1):
            memo[0][i] = v[0] if i >= w[0] else 0
        for time in range(1, len(w)):
            for cap in range(c + 1):
                i, j = (1, 0) if time & 1 else (0, 1)
                memo[j][cap] = memo[i][cap]
                if cap >= w[time]:
                    memo[j][cap] = max([memo[j][cap], v[time] + memo[i][c - w[time]]])
        return memo[-1][-1]


s = Solution()
re = s.knapsack01_ADM([1, 2, 3], [6, 10, 12], 5)
print(re)
