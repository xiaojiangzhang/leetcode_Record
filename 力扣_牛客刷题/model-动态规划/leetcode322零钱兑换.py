"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
问题：考虑将n个银币组合成金额m
F(n,m)= min(F(n-1,m)||1+F(n,m-w(n))
"""


class Solution:
    def coinChange(self, coins, amount):
        memo = [float("INF")] * (amount + 1)

        def dp(a):
            if a < 0:
                return -1
            if a == 0:
                return 0
            if memo[a] != float("INF"):
                return memo[a]
            res = float('INF')
            for coin in coins:
                subPro = dp(a - coin)
                if subPro == -1:
                    continue
                res = min([subPro + 1, res])
            memo[a] = res
            return res if res != float('INF') else -1

        return dp(amount)

    def coinChange2(self, coins, amount):
        if amount == 0 or len(coins) == 0:
            return -1
        memo = [float("INF")] * (amount + 1)
        memo[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                memo[i] = min([memo[i], 1 + memo[i - coin]])
        return memo[amount] if memo[amount] != float("INF") else -1


s = Solution()
res = s.coinChange2(coins=[2], amount=3)
print(res)
