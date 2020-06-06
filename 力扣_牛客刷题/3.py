'''现有一个语音识别模型，可以对音频预测出正确的文字，但是偶尔有错误，会出现漏字、多字、错字情况，需要一个方法来评价，评价方法为：

1-（预测文字和正确文字的编辑距离）/正确文字的个数，计算之前扣除所有标点符号

结果请四舍五入保留四位小数
输入
正确文字和预测文字在一行，中间以一个空格 隔开如

携程欢迎您 携程欢迎

输出
由于少一个字，1-1/5=0.8000，结果请四舍五入保留四位小数

0.8000


样例输入
携程欢迎您 携程欢迎
样例输出
0.8000
'''
import sys

data = sys.stdin.readline().strip()
label, pre = map(str, data.split(' '))
distence = 0
y = label
i = 0
while i < len(pre):
    if pre[i] == label[i]:
        i += 1
        pre = pre[1:]
        label = label[1:]
distence = len(label) - i
score = 1 - distence / len(y)
print(round(score, 4))
