# -*- coding: utf-8 -*-

'''
Sudoku Solver
=============

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''


class Solution(object):
    '''算法思路：

    DFS + 回溯，用 rows, cols, grids 分别表示水平，垂直，宫格状态，lack 表示还有几个格子
    没填，也可以不用 lack，判断 i 是否 >= 9，即可以知道是否结束
    '''
    def dfs(self, board, i, j, rows, cols, grids):
        if i >= 9:
            return True

        if board[i][j] != '.':
            return self.dfs(
                board, i + (j + 1) // 9, (j + 1) % 9, rows, cols, grids)

        for candidate in range(1, 10):
            mask = 1 << candidate
            if (rows[i] & mask) + (cols[j] & mask) + (
                    grids[i//3][j//3] & mask) == 0:

                board[i][j] = str(candidate)
                rows[i] |= mask
                cols[j] |= mask
                grids[i//3][j//3] |= mask

                if self.dfs(
                        board, i + (j + 1)//9, (j + 1) % 9, rows, cols, grids):
                    return True

                board[i][j] = '.'
                rows[i] &= ~mask
                cols[j] &= ~mask
                grids[i//3][j//3] &= ~mask

        return False

    def solveSudoku(self, board):
        rows, cols, grids = [0] * 9, [0] * 9, [[0] * 3 for _ in range(3)]
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == '.':
                    continue

                mask = 1 << ord(char) - 48

                rows[i] |= mask
                cols[j] |= mask
                grids[i//3][j//3] |= mask

        self.dfs(board, 0, 0, rows, cols, grids)


s = Solution()
print s.solveSudoku([
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
])
