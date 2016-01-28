# -*- coding: utf-8 -*-

'''
Maximal Square
==============

Given a 2D binary matrix filled with 0's and 1's, find the largest square
containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.
'''


class Solution(object):
    '''算法思路：

    对于每一个值为 '1' 的 (i, j)，求出其最大宽度，然后得到总体最大宽度

    结果：勉强 AC
    '''
    def check(self, i, j, matrix, width):
        xStart, yStart = i - width + 1, j - width + 1

        if xStart < 0 or yStart < 0:
            return False

        return all(
            x - xStart + y - yStart >= width or matrix[x][y] == '1'
            for x in xrange(xStart, i + 1)
            for y in xrange(yStart, j + 1)
        )

    def findMaxWidth(self, i, j, matrix):
        width = 1
        while 1:
            if not self.check(i, j, matrix, width + 1):
                break
            width += 1
        return width

    def maximalSquare(self, matrix):
        maxWidth = max([
            self.findMaxWidth(i, j, matrix)
            for i, row in enumerate(matrix)
            for j, num in enumerate(row) if num == '1'
        ] or [0])
        return maxWidth * maxWidth


class Solution(object):
    '''算法思路：

    动态规划，dp[i][j] 是以 (i, j) 为右下角的最长正方形的边长

    结果：AC
    '''
    def maximalSquare(self, matrix):
        m, n = len(matrix), len(matrix[0]) if matrix else 0

        dp, maxWidth = [[0] * (n + 1) for _ in xrange(m + 1)], 0
        for i, row in enumerate(matrix, 1):
            for j, num in enumerate(row, 1):
                if num == '1':
                    dp[i][j] = min(
                        dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxWidth = max(dp[i][j], maxWidth)
        return maxWidth * maxWidth


s = Solution()
square = [
    '1 0 1 0 0'.split(' '),
    '1 0 1 1 1'.split(' '),
    '1 1 1 1 1'.split(' '),
    '1 0 0 1 0'.split(' ')
]
print s.maximalSquare([])
