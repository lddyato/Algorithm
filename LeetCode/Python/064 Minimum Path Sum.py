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
        m, n = map(len, (grid, grid[0]))
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = (dp[i - 1][0] if i else 0) + grid[i][0]

        for j in range(n):
            dp[0][j] = (dp[0][j - 1] if j else 0) + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]
