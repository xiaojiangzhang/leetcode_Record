# 输入:输入任意一串字符
# 样例输入:aaaabbcd
#
# 输出:计算出字符串的信息熵
# 样例输出:1.75
#
# 信息熵的计算公式为：某一事件出现的概率乘以它的对数形式的结果的负数就是该时间的信息熵，把一个集合里面的所有的事件的信息熵都加起来就行了，就可以得到了总的信息熵了，明白了这一点就很容易做这道题目了，因为计算量很小，所以代码几乎就是直接写出来的没有做一点性能上的优化，不过结果AC了，应该是输入的数据量规模也是不大的：
from collections import Counter
import math

in_str = input()
count = Counter(in_str)
ent = 0
for key, coun in count.items():
    p = float(coun) / len(in_str)
    ent += -1 * p * math.log(p, 2)
print (round(ent,7))
