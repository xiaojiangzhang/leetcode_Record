"""
题目描述：
n个数的伪中位数定义为从小到大排序后第⌊(n+1)/2⌋个数。其中，⌊x⌋的意思是x向下取整。

现在，给你n个数，你需要向其中增加最少的数，使得k成为最后这一组数的伪中位数。

请问你需要加入数的最少数。

输入
输入第一行包含两个数n,k,意为原来数的个数和最后的伪中位数。

接下来一行n个数a_i，空格隔开，代表原来的数。

1≤n≤500,1≤a_i≤100000

输出
输出一个数，你需要加入数的最少数量。


样例输入
4 2
2 3 3 3
样例输出
2

提示
样例解释：加入1,1后,原数组变为1,1,2,3,3,3,其伪中位数为2。
"""
import sys


def fuct(n, k):
    if n <= 0 or k == 0 or n > 500:
        return 0
    input2 = sys.stdin.readline().strip()
    nums = list(map(int, input2.split(' ')))
    if max(nums) > 100000:
        return 0
    if k not in nums:
        nums.append(k)
        nums.sort()
        index = nums.index(k)
        left = len(nums) - index - 1
        return left - index if left >= index else index - left
    nums.sort()
    index = nums.index(k)

    left = len(nums) - index - 1
    return left - index if left >= index else index - left


input = sys.stdin.readline().strip()
n, k = list(map(int, input.split(' ')))
res = fuct(n, k)
sys.stdout.write(str(res-1))
