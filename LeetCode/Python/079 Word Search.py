# -*- coding: utf-8 -*-

'''
Word Search
===========

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''


class Solution(object):
    '''算法思路：

    DFS
    '''
    def dfs(self, board, m, n, i, j, word, p):
        '''
        Params:
          - board: 当前 board 状态，已经访问过的设置为 None
          - m: board 行数
          - n: board 列数
          - i: 当前遍历的的地方行数
          - j: 当前遍历到的地方列数
          - word: 查询的单词
          - p: 当前查询 word 的第几个字母
        '''
        if p >= len(word):
            return True

        char, board[i][j] = board[i][j], None
        for x, y in ((0, 1), (-1, 0), (0, -1), (1, 0)):
            ii, jj = i + x, j + y
            if (0 <= ii < m and 0 <= jj < n and board[ii][jj] == word[p] and
                    self.dfs(board, m, n, ii, jj, word, p + 1)):
                return True

        board[i][j] = char
        return False

    def exist(self, board, word):
        m, n = map(len, (board, board[0]))
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == word[0] and self.dfs(board, m, n, i, j, word, 1):
                    return True
        return False


s = Solution()
board = [
  ['A','A'],
]
print s.exist(board, 'AAA')
