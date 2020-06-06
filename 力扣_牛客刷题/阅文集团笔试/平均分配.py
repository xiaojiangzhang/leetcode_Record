class Solution:
    def canPartition(self, nums):
        # 定义状态描述dp[i][0] dp[i][1]
        # 其中dp[i][0]表示第1个队伍的物资，dp[i][1]表示第二个队伍的物资
        if len(nums) <= 1:
            return False
        s = sum(nums)
        if s % 2 != 0:
            return False
        c = int(s / 2)
        memo = [False] * (c + 1)
        for i in range(c + 1):
            memo[i] = True if nums[0] == i else False
        for i in range(1, len(nums)):
            for j in range(c, nums[i] - 1, -1):
                memo[j] = memo[j] | memo[j - nums[i]]
        return memo[-1]


s = Solution()
res = s.canPartition([1, 1, 11, 5])
print(res)
