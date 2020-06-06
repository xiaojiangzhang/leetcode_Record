"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        leng = [len(i) for i in strs]
        min_len_index = leng.index(min(leng))
        min_char = strs[min_len_index]
        res = 0
        for i in range(len(min_char)):
            char = min_char[i]
            flag = False
            for s in strs:
                if s[i] == char:
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                res += 1
            else:
                break
        return min_char[:res]


s = Solution()
res = s.longestCommonPrefix(["aca", "cba"])
print(res)
