"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
考虑将n个物品填满容量为c的背包
状态转移方程：F（i,c） = F（i-1,c)||F(i,c-w(i))
'''


class Solution:
    def canPartition(self, nums):
        if len(nums) <= 1:
            return len(nums)
        c = int(sum(nums) / 2)
        if sum(nums) % 2 != 0:
            return False
        self.memo = [[-1 for _ in range(c + 1)] for _ in range(len(nums))]
        return self.dp(len(nums) - 1, nums, c) == 1

    def dp(self, index, nums, c):
        if c == 0:
            return True
        if index < 0 or c < 0:
            return False
        if self.memo[index][c] != -1:
            return self.memo == 1
        self.memo[index][c] = 1 if self.dp(index - 1, nums, c) or self.dp(index - 1, nums, c - nums[index]) else 0
        return self.memo[index][c]

    def dp2(self, nums):
        if len(nums) <= 1:
            return len(nums)
        c = int(sum(nums) / 2)
        if sum(nums) % 2 != 0:
            return False
        memo = [[False for _ in range(c + 1)] for _ in range(len(nums))]
        # 状态转移方程：F（i, c） = F（i - 1, c) | | F(i-1, c - w(i))
        # baseCase
        for i in range(c + 1):
            memo[0][i] = (nums[0] == i)
        # print(memo[0][12])
        for i in range(1, len(nums)):
            for j in range(c, -1, -1):
                memo[i][j] = memo[i - 1][j] | memo[i - 1][j - nums[i]]
        return memo[-1][-1]

    # 空间优化
    def dp3(self, nums):
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
            for j in range(c, nums[i]-1, -1):
                memo[j] = memo[j] | memo[j - nums[i]]
        return memo[-1]


s = Solution()
res = s.dp3([1, 5, 11, 1, 1, 5])
print(res)
