# -*- coding: utf-8 -*-

'''
Longest Increasing Path in a Matrix
===================================

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or
down. You may NOT move diagonally or move outside of the boundary (i.e.
wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''


class Solution(object):
    '''算法思路：

    DFS + Backtracing
    '''
    def search(self, i, j, val, m, n, matrix, r):
        if r[i][j] is not None:
            return r[i][j]

        length = 0
        for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            ii, jj = i + x, j + y
            if 0 <= ii < m and 0 <= jj < n and matrix[ii][jj] > val:
                v = matrix[ii][jj]

                matrix[ii][jj] = float('-inf')
                length = max(self.search(ii, jj, v, m, n, matrix, r), length)
                matrix[ii][jj] = v

        r[i][j] = length + 1
        return r[i][j]

    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        r = [[None] * n for _ in xrange(m)]

        return max(
            self.search(i, j, val, m, n, matrix, r)
            for i, row in enumerate(matrix)
            for j, val in enumerate(row)
        )


nums = [
  [1,2,3],
  [3,1,4],
  [7,6,5]
]

s = Solution()
print s.longestIncreasingPath(nums)
