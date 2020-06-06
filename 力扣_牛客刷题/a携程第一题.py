"""题目描述：
给定一个由 n 个小写英文字母组成的字符串 s = s1 ... sn ，另给定 k 个各不相同的英文字母，
计算在所有 s 的子字符串中有多少可以由这 k  个字母或这 k  个字母的子集组成。(相同子字符串视为多个子字符串)

输入
第一行为空格分开的两个数字代表 n  和 k  。( 1 <= n <= 105 , 1 <= k <= 26 )

第二行为字符串 s 。

第三行为 k 个由空格分隔开的小写英文字母。

输出
子字符串数量。
"""
import sys


def num_sub_Str(str):
    sub = []
    for i in range(len(str)):
        for j in range(i, len(str)):
            sub.append(str[i:j + 1])
    return sub


s = num_sub_Str('abcad')
k = 'ab'
# for sub in s:
#

print(s)
