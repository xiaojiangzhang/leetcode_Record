'''
平行线段
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
给出平面上的2n个点，你可以将这2n个点每两个匹配到一起得到n条线段。

请你计算一种匹配方式，使得你得到的这n条线段，平行的线段对数最多。

输入
第一行包含一个整数2n，2 <= 2n <= 16。

接下来2n行，每行包含两个整数x, y，表示一个点的坐标。

-1000 <= x, y <= 1000

保证所有的点都不重合，并且没有三点共线

输出
输出最多能有多少对线段平行。


样例输入
8
0 0
0 5
2 2
2 7
3 -2
5 0
4 -2
8 2
样例输出
6

提示
这8个点可以组成4条两两平行的线段，所以最多可以有6对平行线段
'''
import sys

n = int(input())
data = []
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    data.append(list(map(int, line.split(' '))))


def dp(n, data):
    if n == 0:
        return 0
    if not 2 <= n <= 16 :
        return 0
    res = []
    for i in range(n):
        for j in range(i, n):

            if (data[j][0] - data[i][0]) == 0 or data[i][1] - data[j][1] == 0:
                res.append(0)
            else:
                res.append((data[i][1] - data[j][1]) / (data[i][0] - data[j][0]))
    res_set = list(set(res))
    r = [0 for _ in range(len(res_set))]
    res_set.remove(0)
    for i in range(len(res_set)):
        for j in range(len(res)):
            if res_set[i] == res[j]:
                r[i] += 1

    return sum([i for i in range(max(r))])


re = dp(n, data)
sys.stdout.write(str(re))
