'''
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections


class Solution:
    def minWindow(self, s: str, t: str):
        left, right = 0, 0
        windiow = {}
        need = {}
        for n in t:
            need[n] = need.get(n, 0)+1
        valid = 0
        start = 0
        length = float("INF")
        while right < len(s):
            c = s[right]
            right += 1
            if need.get(c):
                windiow[c] = windiow.get(c, 0) + 1
                if windiow.get(c) == need.get(c):
                    valid += 1
            print(left, right, valid,length)
            # 判断左侧窗口是否需要收缩
            while valid == len(need):
                # 更新最小覆盖子串
                if right - left < length:
                    start = left
                    # print(left)
                    length = right - left
                # d为将要移出滑动窗口的字符
                d = s[left]
                left += 1
                if need.get(d):
                    if windiow.get(d) == need.get(d):
                        valid -= 1
                    windiow[d] = windiow.get(d) - 1
        return s[start:start + length] if length != float("INF") else ""


s = Solution()
res = s.minWindow(s="aa", t="aa")
print(res)
