class Solution:
    def minWindow(self, s: str, t: str):
        window = {}
        target = {}
        vailds = 0
        start = 0
        length = float("INF")
        for i in t:
            target[i] = target.get(i, 0) + 1
        left, right = 0, 0
        while right < len(s):
            # 第一层循环的目标是将滑动窗口扩大到包含所有的目标元素
            # 当前准备添加到滑动窗口中的元素
            c = s[right]
            right += 1
            # 判断c是否为目标元素
            if target.get(c, 0):
                # 在window中查找c元素，加1
                window[c] = window.get(c, 0) + 1
                if window[c] == target[c]:
                    vailds += 1
            # 当滑动窗口中包含所有目标元素，缩小滑动窗口的左边界
            while vailds == len(target):

                if right - left < length:
                    start = left
                    length = right - left
                # 将待出滑动窗口元素d进行判断
                d = s[left]
                left += 1
                # 如果待出窗口元素d为目标元素，则将滑动窗口中的目标元素减一，同时将vailds已匹配元素减一
                if target.get(d, 0):
                    if window[d] == target[d]:
                        vailds -= 1
                    window[d] -= 1

        return s[start:start + length] if length != float("INF") else ""


s = Solution()
res = s.minWindow("ADOBECODEBANC", "ABC")
print(res)
