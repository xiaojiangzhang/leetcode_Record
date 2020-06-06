'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

'''


class Solution:

    def numDecodings(self, s):
        # if (s) == '0':
        #     return 0
        self.emenu = [-1 for _ in range(len(s) + 1)]
        return self.decodeNum(s, 0, len(s) - 1)

    def decodeNum(self, s, l, r):
        print(l)
        if l >= r:
            return 1
        if self.emenu[l] != -1:
            return self.emenu[l]

        if s[l] == '0':
            return 0
        pre = self.decodeNum(s, l + 1, r)
        if s[l] + s[l + 1] <= '26':
            pre += self.decodeNum(s, l + 2, r)
        self.emenu[l] = pre
        return pre


s = Solution()
re = s.numDecodings("10")
print(re)
