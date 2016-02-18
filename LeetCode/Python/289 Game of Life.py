# -*- coding: utf-8 -*-

'''
Game of Life
============

According to the Wikipedia's article: "The Game of Life, also known simply as
Life, is a cellular automaton devised by the British mathematician John Horton
Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or
dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
diagonal) using the following four rules (taken from the above Wikipedia
article):

- Any live cell with fewer than two live neighbors dies, as if caused by
  under-population.
- Any live cell with two or three live neighbors lives on to the next
  generation.
- Any live cell with more than three live neighbors dies, as if by
  over-population..
- Any dead cell with exactly three live neighbors becomes a live cell, as if by
  reproduction.

Write a function to compute the next state (after one update) of the board
given its current state.

Follow up:
- Could you solve it in-place? Remember that the board needs to be updated at
  the same time: You cannot update some cells first and then use their updated
  values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the
  board is infinite, which would cause problems when the active area encroaches
  the border of the array. How would you address these problems?
'''


import copy


class Solution(object):
    '''算法思路：

    根据题意遍历即可，不过，用了额外的 O(m*n) 空间
    '''
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])

        duplicate = copy.deepcopy(board)
        for x, row in enumerate(duplicate):
            for y, num in enumerate(row):
                lives = dies = 0
                for i, j in [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1),
                             (1, 1), (1, 0), (1, -1)]:
                    if 0 <= x + i < m and 0 <= y + j < n:
                        if duplicate[x + i][y + j]:
                            lives += 1
                        else:
                            dies += 1

                if num and lives < 2 or lives > 3:
                    board[x][y] = 0
                elif not num and lives == 3:
                    board[x][y] = 1


s = Solution()
s.gameOfLife([[1,1],[1,0]])
