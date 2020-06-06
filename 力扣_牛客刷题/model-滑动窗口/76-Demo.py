class Solution:
    def minWindow(self, s: str, t: str):
        window, target = {}, {}
        left, right, start = 0, 0, 0
        vailds = 0
        length = float('INF')
        for i in t: target[i] = target.get(i, 0) + 1
        while right < len(s):
            # 将待放入滑动窗口中的字符c取出
            c = s[right]
            right += 1
            # 如果c是目标字符的话，将其添加到窗口中
            if target.get(c, 0):
                window[c] = window.get(c, 0) + 1
                # 如果window中c的个数等于目标字符个数，vailds+1
                if target[c] == window[c]:
                    vailds += 1
            # 判断已经匹配的字符个数是否等于目标字符个数
            while vailds == len(target):
                if right - left < length:
                    length = right - left
                    start = left
                d = s[left]
                left += 1
                if target.get(d, 0):
                    if window[d] == target[d]:
                        # window[d] -= 1
                        vailds -= 1
                    window[d] -= 1
        return s[start:start + length] if length != float("INF") else ""


s = Solution()
res = s.minWindow("ADOBECODEBANC", "ABC")
print(res)
