# -*- coding: utf-8 -*-

'''
Unique Paths
============

A robot is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below).

The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

How many possible unique paths are there?
'''


import math


class Solution(object):
    '''算法思路：

    组合问题, from m+m-2 elements choose m-1 elements

    Time: O(1)
    Space: O(1)
    '''
    def uniquePaths(self, m, n):
        return reduce(
            lambda x, y: x and x / y or y,
            map(math.factorial, (m + n - 2, m - 1, n - 1)))


class Solution(object):
    '''算法思路：

    dp，设 dp[i][j] 是从 (0, 0) 到 (i, j) 处所需的步数，则：

    dp[i][j] = dp[i-1][j] + dp[i][j-1]

    Time: O(m*n)
    Space: O(m*n)
    '''
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                dp[i][j] = max(dp[i - 1][j] + dp[i][j - 1], 1)

        return dp[m - 1][n - 1]


s = Solution()
print s.uniquePaths(3, 7)
