""""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time


class Solution:
    # 记忆搜索
    def rob(self, nums):
        self.record = [-1 for _ in range(len(nums))]
        if nums == None:
            return
        return self.Robber(nums, 0)

    def Robber(self, nums, start):
        if start >= len(nums):
            return 0
        if self.record[start] != -1:
            return self.record[start]
        res = -1
        for i in range(start, len(nums)):
            res = max([res, nums[i] + self.Robber(nums, i + 2)])
        self.record[start] = res
        return res

    # 递归实现
    def rob2(self, nums):
        if nums == None:
            return
        return self.Robber2(nums, 0)

    def Robber2(self, nums, start):
        if start >= len(nums):
            return 0
        res = -1
        for i in range(start, len(nums)):
            res = max([res, nums[i] + self.Robber2(nums, i + 2)])
        return res

    def rob3(self, nums):
        return self.Robber3(nums)

    def Robber3(self, nums):
        n = len(nums)
        memo = [-1 for _ in range(n)]
        memo[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(i, n):
                # if j + 2 < n:
                memo[i] = max([memo[i], nums[j] + (memo[j + 2] if j + 2 < n else 0)])
            # else:
            #     memo[i] = max([memo[i], nums[j]])
        return memo[0]


q = [2, 7, 9, 3, 1]
s = Solution()
start = time.perf_counter()
re = s.rob(q)
end = time.perf_counter()
print('max value is ', re)
print('times is : ', end - start)

start = time.perf_counter()
re = s.rob2(q)
end = time.perf_counter()
print('max value is ', re)
print('times is : ', end - start)

start = time.perf_counter()
re = s.rob3(q)
end = time.perf_counter()
print('max value is ', re)
print('times is : ', end - start)
