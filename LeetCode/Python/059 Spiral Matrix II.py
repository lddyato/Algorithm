# -*- coding: utf-8 -*-

'''
Spiral Matrix II
================

Given an integer n, generate a square matrix filled with elements from 1 to n^2
in spiral order.

For example,
Given n = 3,

You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''


class Solution(object):
    '''算法思路：

    一圈一圈的生成
    '''
    def generateMatrix(self, n):
        start, row, col, matrix = 1, 0, 0, [[0] * n for _ in xrange(n)]
        while n > 0:
            i = j = 0
            for index, iterator in enumerate([
                    xrange(n),
                    xrange(1, n),
                    xrange(n - 2, -1, -1),
                    xrange(n - 2, 0, -1)]):
                for x in iterator:
                    if index & 1:
                        i = x
                    else:
                        j = x
                    matrix[row + i][col + j] = start
                    start += 1
            row += 1
            col += 1
            n -= 2
        return matrix


class Solution(object):
    """算法思路：

    同上，只不过是另外一种写法
    """
    def generate(self, x, y, w, start, board):
        i, j = 0, 0
        for j in xrange(w):
            board[x + i][y + j] = start
            start += 1

        for i in xrange(1, w):
            board[x + i][y + j] = start
            start += 1

        if w > 1:
            for j in xrange(w - 2, -1, -1):
                board[x + i][y + j] = start
                start += 1

            for i in xrange(w - 2, 0, -1):
                board[x + i][y + j] = start
                start += 1

        return start

    def generateMatrix(self, n):
        board = [[0] * n for _ in xrange(n)]

        x, y, start = 0, 0, 1
        while n > 0:
            start = self.generate(x, y, n, start, board)
            x += 1
            y += 1
            n -= 2

        return board


s = Solution()
print s.generateMatrix(3)
