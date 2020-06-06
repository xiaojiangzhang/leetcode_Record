class Solution:
    def Valid(self, m, n):
        while m != n:
            if m > n:
                m = m - n
            else:
                n = n - m
        return False if m <= 1 else True

    def splitArray(self, nums):
        #         状态 f（0...i） = f(1...i-1), f(0...i)
        if len(nums) == 0:
            return 0
        res = float('INF')
        memo = [[0for _ in range(len(nums))] for _ in range(len(nums))]
        print(memo)
        def back(res, nums, start, end):
            if memo[start][ end] != 0:
                return memo[start][end]
            print(start, end)
            if start > end:
                return float('INF')
            if self.Valid(nums[start], nums[end]):
                return 0
            res = back(res, nums, start, end - 1) + 1
            res = min(res + back(res, nums, start + 1, end) + 1, back(res, nums, start + 1, end - 1) + 1)
            memo[start][end] = res
            return res

        res = back(res, nums, 0, len(nums) - 1)
        print(res)
        return res + 1


s = Solution()
res = s.splitArray([2, 3, 3, 2, 3, 3])
print(res)
