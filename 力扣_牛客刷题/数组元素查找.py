# 数组元素查找
'''
 给定一个整形数组，请写一个算法，找到第一个仅出现一次的数组元素，复杂度O(n) 。
 样例输入
1,1,2,2,3,3,4,4,5,6,6,8,9,9
样例输出
5
'''
from collections import Counter

string = input()
count = Counter(string).items()
for key, con in count:
    if con == 1:
        print(key)
        break
