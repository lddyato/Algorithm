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


s = Solution()
print s.generateMatrix(3)
