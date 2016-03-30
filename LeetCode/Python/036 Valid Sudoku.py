# -*- coding: utf-8 -*-

'''
Valid Sudoku
============

Determine if a Sudoku is valid according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with
the character '.'.

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the
filled cells need to be validated.
'''


class Solution(object):
    '''算法思路：

    根据数独特性进行判断即可, 每一行，每一列，每一个九宫格均不能有重复的
    '''
    def isValidSudoku(self, board):
        rows, cols = [[set() for _ in range(9)] for _ in range(2)]
        grid = [[set() for _ in range(3)] for _ in range(3)]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == '.':
                    continue

                if (num in rows[i] or num in cols[j] or
                        num in grid[i // 3][j // 3]):
                    return False

                rows[i].add(num)
                cols[j].add(num)
                grid[i // 3][j // 3].add(num)
        return True


s = Solution()
board = [
    '..5.....6',
    '....14...',
    '.........',
    '.....92..',
    '5....2...',
    '.......3.',
    '...54....',
    '3.....42.',
    '...27.6..'
]
print s.isValidSudoku(board)
