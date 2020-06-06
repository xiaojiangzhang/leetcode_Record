"""

"""
# 状态 怪物数 血量 金币
#       bp[i][0]打第i个怪物时购买或者不够买
# bp[i][0] = bp[i-1][0],bp[i-1][1]-2/w[i]
# bp[i][1] = bp[i-1][1]-2/w[i] ,bp[i-1][0]
#       bp[i][1] = max(bp[i-1][k]-2/w[i], bp[i-1][k])
#     打第i个怪物血量为k，i-1个怪物血量为k-2
# dp表示待求的最值，dp[i][k]表示打第i个怪物时的血量为k的盈利
# dp[i][k] = max(dp[i-1][k], dp[i-1][k-w[i]]-1/n*w[i]+v[i])
# 第i个怪物
data = [[1, 1], [1, 10], [3, 1]]
m, n = 3, 2


def getMax(data, m, n):
    k = sum([i[0] for i in data])
    dp = [[0 for _ in range(k)] for i in range(m)]
    for i in range(m):
        for j in range(k):
            if i == 0:
                dp[i][j] = data[i][1] - 1 / n * data[i][0]
                continue
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - data[i][0]] - (1 / n) * data[i][0] + data[i][1])
    print(dp)
    return dp


def getMax2(data, m, n):
    energy = 0
    coins = 0
    for i in data:
        if i[1] * n > i[0]:
            energy += i[0]
            coins += i[1]
    coins = coins - int(energy / n)
    if energy % n != 0:
        coins -= 1
    return coins


res = getMax2(data, m, n)
print(res)
