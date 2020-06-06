'''
给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import copy


class Solution:
    def totalNQueens(self, n: int):
        res = []

        # 判断当前选择是否合法
        def isValid(board, row, col):
            # 判断当前列中是否有皇后存在
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False
            #  判断左上角是否有皇后
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            # 判断右上角是否有皇后
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtrack(board, row):
            if row == len(board):
                print(board)
                res.append(copy.deepcopy(board))
                return
            for col in range(len(board)):
                if not isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'

        board = [['.' for i in range(n)] for j in range(n)]
        backtrack(board, 0)
        return len(res)


s = Solution()
res = s.totalNQueens(4)
print(res)
