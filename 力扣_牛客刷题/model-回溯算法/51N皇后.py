'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
示例:
输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import copy


class Solution:
    def solveNQueens(self, n: int):
        res = []

        # 是否可以在board[row][col]放置皇后
        def isValid(board, row, col):
            # 检查列是否有皇后冲突
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False
            # 检查右上方是否有皇后互相冲突
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            # 检查左上方是否有皇后冲突
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            return True

        def backtrack(board, row):
            # 触发结束条件
            if row == len(board):
                res.append(copy.deepcopy(board))
                # print(res)
                return
            for col in range(len(board[row])):
                # 排除不合法选择
                if not isValid(board, row, col):
                    continue
                # 做选择
                board[row][col] = 'Q'
                # 进入下一行决策
                backtrack(board, row + 1)
                # 撤销选择
                board[row][col] = '.'

        board = [["." for i in range(n)] for i in range(n)]
        backtrack(board, 0)
        return [["".join(j) for j in i] for i in res]


s = Solution()
res = s.solveNQueens(4)
# res = [["".join(j) for j in i] for i in res]
print(res)
# for i in res:
#     for j in i:
#         print("".join(j))
