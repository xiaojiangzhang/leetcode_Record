'''
有这么一段伪代码

input a,b,m,x

while true:

  x=(a*x+b)%m

  print(x)

end while

输出的x由于是在取模意义下的，所以会出现循环。

比如，a=2, b=1, m=5, x=2的时候，输出的序列将会如下：

0,1,3,2,0,1,3,2,0,1,3,2....

其中：0,1,3,2 称为最短的循环节。

现在给定a,b,m,x的值，请你计算最短循环节的长度。

输入
输入4个数，a,b,m,x

输出
输出一个数，最短循环节的长度


样例输入
2 1 5 2
样例输出
4

提示
1≤a,b,x≤m≤100000 ,a,b,x,m均为正整数
'''
import sys


def find(a, b, m, x):
    if not (a >= 1 and b >= 1 and m >= x and m <= 100000):
        return 0
    res = [0 for _ in range(10)]
    count = 0
    while count <= 100000:
        count += 1
        x = (a * x + b) % m
        res[x] += 1
    re = 0
    for i in res:
        if i != 0:
            re += 1
    return re


input = sys.stdin.readline().strip()
a, b, m, x = list(map(int, input.split(' ')))
res = find(a, b, m, x)
sys.stdout.write(str(res))
