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

    根据数独特性进行判断即可
    '''
    def isValidSudoku(self, board):
        N = 9

        for i in xrange(N):
            record_row, record_col = {}, {}

            for j in xrange(N):
                s_row, s_col = board[i][j], board[j][i]

                record_row[s_row] = record_row.setdefault(s_row, 0) + 1
                record_col[s_col] = record_col.setdefault(s_col, 0) + 1

                if (s_row != '.' and record_row[s_row] > 1) or (
                        s_col != '.' and record_col[s_col] > 1):
                    return False

        for i in xrange(0, 7, 3):
            for j in xrange(0, 7, 3):
                record = {}

                for k in xrange(3):
                    for l in xrange(3):
                        s = board[i + k][j + l]
                        record[s] = record.setdefault(s, 0) + 1
                        if s != '.' and record[s] > 1:
                            return False

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
