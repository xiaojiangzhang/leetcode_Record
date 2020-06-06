'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''
"""
最多只允许完成一次交易，相当于k=1
确定状态和状态下的选择
状态：天数i、是否持有股票01、交易数k
选择：买入，卖出，保持不变
dp[i][k][0]:表示第i天，允许交易数为k，0表示当前没有股票，1表示当前持有股票
状态转移方程：dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1-1][1]+price[i])
              dp[i][1][1] = max(dp[i-1][1][1],dp[i-1][1][0]-price[i])
    发现k都为1，将k简化
              dp[i][0] = max(dp[i-1][0],dp[i-1][1]+price[i])
              dp[i][1] = max(dp[i-1][1],-price[i])
定义base case：
              dp[0][1][0] =               
"""

import sys


class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][1] = -prices[i]
                dp[i][0] = 0
                continue
            dp[i][0] = max([dp[i - 1][0], dp[i - 1][1] + prices[i]])
            dp[i][1] = max([dp[i - 1][1], - prices[i]])
        return dp[n - 1][0]

    # 空间优化，在状态转移方程中，新状态只和相邻的一个状态有关系
    def maxProfit2(self, prices):
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -price[0]
        for i in range(n):
            dp_i_0 = max([dp_i_0, dp_i_1 + prices[i]])
            dp_i_1 = max([dp_i_1, -prices[i]])
        return dp_i_0


price = [7, 1, 5, 3, 6, 4]
s = Solution()
res = s.maxProfit2(price)
print(res)
