class Solution:
    def editDistence(self, s1, s2):
        n = len(s1)
        m = len(s2)
        if n == 0 and m == 0:
            return 0
        if n == 0 or m == 0:
            return n if m == 0 else n
        return self.dis(s1, s2, n - 1, m - 1)

    def dis(self, s1, s2, n, m):
        if n == -1 or m == -1:
            return 0
        if s1[n] == s2[m]:
            return self.dis(s1, s2, n - 1, m - 1)
        else:
            return min([self.dis(s1, s2, n - 1, m) + 1,
                        self.dis(s1, s2, n, m - 1) + 1,
                        self.dis(s1, s2, n - 1, m - 1) + 1])


s = Solution()
res = s.editDistence('horse', 'ros')
print(res)
