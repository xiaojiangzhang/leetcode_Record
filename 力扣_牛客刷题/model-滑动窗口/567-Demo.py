"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def checkInclusion(self, s1, s2):
        target, window = {}, {}
        left, right, start, vailds = 0, 0, 0, 0
        length = float('INF')
        for i in s1: target[i] = target.get(i, 0) + 1
        while right < len(s2):
            c = s2[right]
            right += 1
            if target.get(c, 0):
                window[c] = window.get(c, 0) + 1
                if window[c] == target[c]:
                    vailds += 1
            while vailds == len(target):
                if right - left < length:
                    length = right - left
                    start = left
                d = s2[left]
                left += 1
                if target.get(d, 0):
                    if target[d] == window[d]:
                        vailds -= 1
                    window[d] -= 1

        return True if length == len(s1) else False


s = Solution()
res = s.checkInclusion("ab", "eidbaooo")
print(res)
