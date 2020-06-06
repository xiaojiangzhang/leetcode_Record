'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
示例 1:
输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.

示例 2:
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
'''
import sys
from functools import lru_cache
import time


class Solution:
    def numSquares(self, n):
        emenu = [0 for _ in range(n + 1)]
        return self.help3(n)

    # 递归实现
    def help(self, n):
        print(n)
        if n == 1 or n == 0:
            return n

        num = sys.maxsize
        for i in range(1, n):
            if i * i <= n:
                num = min([num, self.help(n - i * i) + 1])
        return num

    # 加入记忆搜索，避免重复计算次数
    def help2(self, n, emenu):
        if n == 0 or n == 1:
            return n
        if emenu[n] is not 0:
            return emenu[n]
        mini = sys.maxsize
        for i in range(1, n):
            if i * i <= n:
                mini = min([mini, self.help2(n - i * i, emenu) + 1])
        emenu[n] = mini
        return mini

    def help3(self, n):
        record = [sys.maxsize for _ in range(n + 1)]
        record[0] = 0
        record[1] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if j * j <= i:
                    record[i] = min([record[i], record[i - j * j] + 1])
        return record[n]


a = time.perf_counter()
print(Solution().numSquares(12))
print(time.perf_counter() - a)
