'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1:
输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections


class Solution:
    def numIslands(self, grid):
        res = 0
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    res += 1
                    queue = collections.deque([(r, c)])
                    grid[r][c] = '0'
                    while queue:
                        row, col = queue.popleft()
                        for x, y in [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                                queue.append((x, y))
                                grid[x][y] = '0'

        return res


s = Solution()
res = s.numIslands(
    [["1", "1", "1", "1", "0"],
     ["1", "1", "0", "1", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "0", "0", "0"]])
print(res)
