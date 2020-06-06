"""
携程呼叫中心7×24小时帮助旅客解决在途中的各种问题，为了尽可能提升服务质量，公司希望客服人数可以满足所有旅客的来电，不用排队等待人工客服。现在提供客服中心所有的通话记录时间，你能算出最少需要多少名客服吗？
输入
输入一个n表示要输入的通话记录个数，接下来输入n行，每行为逗号相隔的两个整数，两个数字分别代表呼入时间和挂断时间的时间戳。 举例：10,30，表示[10,30)，代表第10秒呼入，第30秒已经挂断，即第30秒可以接入新的来电； 每一行都是一条通话记录，通话记录已经按呼入时间由小到大排序；

输出
输出一个整数；

代表最少需要多少客服，可以满足所有旅客来电不用等待。

样例输入
6
0,30
0,50
10,20
15,30
20,50
20,65
样例输出
5
"""


def get_subNum(num, n):
    count = []
    # num.sort(key=lambda num: num[1])
    for i in range(num[-1][1]):
        coun = 0
        for start, end in num:
            if start < i < end:
                coun += 1
        count.append(coun)
    return max(count)


n = 6
num = [[0, 30], [5, 10], [15, 20]]
# print(get_subNum(num, n))
# print(num[-1])
import heapq

a = [num[0][1]]
heapq.heapify(a)
count = 0
for start, end in num:
    cur = heapq.heappop(a)
    if start < cur:
        heapq.heappush(a, cur)
        count += 1
        heapq.heappush(a, end)
print(count)
