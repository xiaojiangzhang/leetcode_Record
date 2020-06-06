# 给定三角形的数字阵列，选择一条自顶向下的路径，使得沿途的所有数字之和最小

#
# class Solution:
#     def minimumTotal(self, triangle):
#         self.row = len(triangle)
#         self.emenu = [[None for _ in range(self.row)] for _ in range(self.row)]
#
#         return self.help(0, 0, triangle)
#
#     def help(self, level, position, triangle):
#         if level == self.row - 1:
#             return triangle[level][position]
#         if self.emenu[level][position]:
#             return self.emenu[level][position]
#         left = self.help(level + 1, position, triangle)
#         right = self.help(level + 1, position + 1, triangle)
#         self.emenu[level][position] = min([left, right]) + triangle[level][position]
#         return self.emenu[level][position]


#     int row = triangle.size();
#     int[] minlen = new int[row+1];
#     for (int level = row-1;level>=0;level--){
#         for (int i = 0;i<=level;i++){   //第i行有i+1个数字
#             minlen[i] = Math.min(minlen[i], minlen[i+1]) + triangle.get(level).get(i);
#         }
#     }
#     return minlen[0];


class Solution:
    def minimumTotal(self, triangle):
        row = len(triangle)
        milen = []
        for level in range(row - 1, 0, -1):
            for i in range(0, level):
                milen.append(min([milen[i], milen[i + 1]]) + triangle[level][i])

        return milen[0]


a = Solution()
c = a.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
])
print(c)
