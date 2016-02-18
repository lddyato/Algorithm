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

    DFS，用 horizontal，vertical，grid 分别表示水平，垂直，宫格状态，然后从 0 到 80
    一个一个尝试
    '''
    def search(self, count, board, horizontal, vertical, grid):
        while count < 81:
            i, j = divmod(count, 9)
            if board[i][j] == '.':
                break
            count += 1
        else:
            return True

        for candidate in xrange(1, 10):
            shift = 1 << candidate
            if not (horizontal[i] & shift or vertical[j] & shift or
                    grid[i/3][j/3] & shift):

                board[i][j] = str(candidate)
                horizontal[i] |= shift
                vertical[j] |= shift
                grid[i/3][j/3] |= shift

                if self.search(count + 1, board, horizontal, vertical, grid):
                    return True

                shift = ~shift

                board[i][j] = '.'
                horizontal[i] &= shift
                vertical[j] &= shift
                grid[i/3][j/3] &= shift

        return False

    def solveSudoku(self, board):
        horizontal, vertical, grid = [1]*9, [1]*9, [[1]*3 for _ in xrange(3)]

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == '.':
                    continue

                shift = 1 << ord(val) - 48

                horizontal[i] |= shift
                vertical[j] |= shift
                grid[i/3][j/3] |= shift

        self.search(0, board, horizontal, vertical, grid)


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
