import collections


class Solution:
    def jiecheng(self, n):
        res = 1
        for i in range(1, n - 1):
            res *= i
        return res


    def expectNumber(self, scores):
        if len(scores) == 0:
            return 0
        count = collections.Counter(scores)
        res = 0
        for key in count:
            if count[key] == 1:
                res += 1
            else:
                c = self.jiecheng(count[key])
                res += 1
        return res


s = Solution()
res = s.expectNumber([1, 1,1, 3])
print(res)
