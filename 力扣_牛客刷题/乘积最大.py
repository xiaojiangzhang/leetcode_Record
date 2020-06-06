# 有一个正整数N可以分解成若干个正整数之和，问如何分解能使这些数的乘积最大？
# 这个题若无整数条件限制，其实答案是全部分解为e（2.71828的那个e）
# 拿到此题，想起了天平称小球问题：n个球中有一个是轻的,试问：怎样用一个没有砝码的天平,用最少的次数找出是哪个球,请算出最少次数。这个题的答案是：当 log3（n）为整数时，最少称log3（n）次，否则，最少称（   [log3(n)]+1   ）次。
# 于是乎，猜测本题应该是将N尽量分解为若干个3，直到不能分解出3，再做出适当的调整。
# 就本题而言，易知，N必为 3n型、3n+1型、3n+2型中的一种（由数论的基本知识知：一个数 mod q，所得数值必在0到q - 1之间），N为3n型数据时，直接全部分解为3；N为3n+1型数据时，最后会出现4，对4不做分解；N为3n+2型数据时，最后会出现5，将5分解为3和2。而N能分解成[N/3]个3。

# 分解成相同自然数
def getMax(num):
    k = int(num / 3)
    if num == 1:
        return 1
    if num % 3 == 0:
        return pow(3, k)
    if num % 3 == 1:
        return 4 * pow(3, k - 1)
    else:
        return 2 * pow(3, k)


# 分解成不同自然数
def getDiffNum(A):
    B = [0 for i in range(100)]
    k = 2
    i = 0
    while A > k:
        B[i] = k
        A = A - k
        k = k + 1
        i = i + 1

    if A > 0:
        for k in range(A):
            B[i - 1 - k] = B[i - 1 - k] + 1
    s = 1
    for j in range(i):
        s = s * B[j]
    return s

num = int(input())
print(getDiffNum(num))
