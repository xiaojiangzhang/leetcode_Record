# 携程身为中国最大的在线旅游服务平台，业务线覆盖广泛、产品池异常丰富，所以用户的选择面大而全。假设某位用户打开了携程App进入首页，
# 他可从多个入口进行选择。若他选择第一个入口，则在进入后a秒便可找到满意的产品从而下单；若他选择第二个入口，则在进入后b秒又会返回首页；
# 若他选择第三个入口，则在进入后c秒又会返回首页。假设用户每次选择都是独立随机的，且下单所需要的时间为x秒，求x的期望。
'''
样例输入
3 5 7
样例输出
15
'''

import sys

a, b, c = sys.stdin.readline().strip().split(' ')
print(int(a) +int(b) +int(c) )
