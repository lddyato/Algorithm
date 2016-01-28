# -*- coding: utf-8 -*-

'''
Minimum Path Sum
================

Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''


class Solution(object):
    '''算法思路：

    dp，dp[i][j] 表示从 (0, 0) 到 (i, j) 路径中的最小和
    '''
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                dp[i][j] = (0 if not i + j else min(
                    dp[i][j - 1] if j > 0 else float('inf'),
                    dp[i - 1][j] if i > 0 else float('inf'))) + grid[i][j]
        return dp[m - 1][n - 1]

