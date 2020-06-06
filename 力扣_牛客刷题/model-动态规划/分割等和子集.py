"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
for i in 状态：
    for j in 选择：
子集背包问题：将一堆有重量的物品放入大小相同的两个背包中。
背包大小为sum(w)/2
dp[i][j]表示前i个物品背包容量为j时有一种方法可以装满
"""


class Solution:
    def canPartition(self, nums):
        n = sum(nums)
        if n % 2 is not 0:
            return False
        n = int(n / 2)
        dp = [[False] * (n + 1) for _ in range(len(nums) + 1)]
        # base line 当背包容量为0的时候可以装满
        for i in range(len(nums)):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, n + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp[-1][-1]

    def canPartition2(self, nums):
        n = int(sum(nums) / 2)
        # dp[i][j]表示前i个物品，背包容量为j时是否可以装下
        dp = [[False] * (n + 1) for _ in range(len(nums) + 1)]
        for d in dp:
            d[0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, n + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

    def canPartition3(self, nums):
        n = sum(nums)
        if n % 2 is not 0:
            return False
        n = int(n / 2)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(len(nums)):
            for j in range(n, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] | dp[j - nums[i]]
        return dp[-1]

s = Solution()
res = s.canPartition3([1, 5, 11, 5])
print(res)
