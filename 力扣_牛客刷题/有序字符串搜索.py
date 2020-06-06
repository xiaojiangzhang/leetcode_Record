'''
给定一些字符串，请写一个算法，从中搜索出包含您输入的字符序列的那些字符串，按匹配度的高低排序输出。没有任何一个字符串匹配上，输出-1。
字符串源source 如下：
"AB",
"ABC",
"ACB",
"ABCD",
"ADBCF",
"ABDCF",
"ABDC",
"ABDFCG",
"ABDFGC",
"ABDEFG",
"GABCEFG"

若输入查找的有序字符序列为"ABC"，则运算结果如下（请注意结果的排序规则）。
ABC         （匹配    ABC）(完全匹配上，匹配度最大)
ABCD      （匹配    ABC.）
ABDC      （匹配    AB.C）
ABDCF    （匹配    AB.C.）
ABDFCG （匹配    AB..C.）
ABDFGC （匹配    AB...C）
ADBCF    （匹配   A.BC.）
GABCEFG（匹配  .ABC...）
'''


def isMattch(str1, str2):
    subNum = 0
    r = 0
    for i in range(len(str1)):
        for j in range(i, len(str2)):
            if str2[j] == str1[i] and i == j:
                subNum += 1
                r += 1
            elif str2[j] == str1[i]:
                r += 1

    if r == len(str1) - 1:
        return None
    subNum = round((subNum / (len(str2) - 1)), 4)
    return [subNum, str2]


mat = input()
source = ["AB",
          "ABC",
          "ACB",
          "ABCD",
          "ADBCF",
          "ABDCF",
          "ABDC",
          "ABDFCG",
          "ABDFGC",
          "ABDEFG",
          "GABCEFG"]
result = []
for i in source:
    re = isMattch(mat, i)
    if re is not None:
        result.append(isMattch(mat, i))
result.sort()
result.reverse()

if result:
    for i in result:
        print(i[1])
else:
    print(-1)
