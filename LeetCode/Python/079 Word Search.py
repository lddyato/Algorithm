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
    def search(self, board, word, visited, i, j, m, n):
        if not word:
            return True

        visited[i][j] = 1

        for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            ii, jj = i + x, j + y
            if (0 <= ii < m and 0 <= jj < n and board[ii][jj] == word[0] and
                    not visited[ii][jj]):
                visited[ii][jj] = 1

                if self.search(board, word[1:], visited, ii, jj, m, n):
                    return True

                visited[ii][jj] = 0

        visited[i][j] = 0
        return False

    def exist(self, board, word):
        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in xrange(m)]

        return any(
            self.search(board, word[1:], visited, i, j, m, n)
            for i, row in enumerate(board)
            for j, char in enumerate(row)
            if word[0] == char
        )


s = Solution()
board = [
  ['A','A'],
]
print s.exist(board, 'AAA')
