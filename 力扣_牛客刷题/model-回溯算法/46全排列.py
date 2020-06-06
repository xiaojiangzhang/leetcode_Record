'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:

    def permute(self, nums):
        track = []
        res = []

        def backtrack(nums, track):
            if len(nums) == len(track):
                res.append(list(track))
                return
            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                backtrack(nums, track)
                track.pop()

        backtrack(nums, track)
        return res

    def getres(self):
        a = [111]
        self.res.append(a)
        return self.res


s = Solution()
res = s.permute([1, 2])
# res = s.getres()
print(res)
