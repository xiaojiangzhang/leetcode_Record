"""给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        return self.sub_seq_len(nums)

    def sub_seq_len(self, num):
        memo = [1 for _ in range(len(num))]
        for i in range(1, len(num)):
            for j in range(i):
                if num[i] > num[j]:
                    memo[i] = max([memo[i], 1 + memo[j]])
        return max(memo)

    def lengthOfLIS2(self, nums):
        if len(nums) == 0:
            return 0
        return self.sub_seq_len2(nums, len(nums) - 1)

    # [10, 9, 2, 5, 3, 7, 101, 18]
    def sub_seq_len2(self, num, index):
        if index == 0:
            return 1
        res = self.sub_seq_len2(num, index - 1)
        if num[index - 1] < num[index]:
            res = max([res, 1 + self.sub_seq_len2(num, index - 1)])

        return res


s = Solution()
re = s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 102, 15])
print(re)
