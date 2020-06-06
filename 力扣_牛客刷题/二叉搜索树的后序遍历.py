# -*- coding:utf-8 -*-
from click._compat import raw_input


class Solution:
    def verifyIsBST(self, sequence, start, end):
        if start >= end: return True
        position = start
        root = sequence[end]
        # 找出分界点
        for position in range(start, end, 1):
            if sequence[position] > root:
                break
        # 在右子树中查看是否存在小于root的值
        if position == end - 1: return True
        for j in range(position, end):
            if sequence[j] < root:
                return False
        return self.verifyIsBST(sequence, start, position - 1) and self.verifyIsBST(sequence, position, end - 1)

    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == None: return False
        return self.verifyIsBST(sequence, 0, len(sequence) - 1)


'''
输入：[1,2,3,4,5]
输出：True
'''
import sys

# 将输入转换为数组
# arr = list(map(int, input().split(" ")))
# print(arr)
#
# # 获取输入字符串
# str = sys.stdin.readline().strip()
# print(str)

# 将输入转化为矩阵
# data = []
# while True:
#     line = sys.stdin.readline().strip()
#     if line:
#         temp = list(map(int, line.split(" ")))
#         data.append(temp)
#     else:
#         break
# print(data)

data = input()
data = list(data)
for i in data:
    print(i)