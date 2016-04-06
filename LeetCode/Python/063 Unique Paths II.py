# -*- coding: utf-8 -*-

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0]) if obstacleGrid else 0
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j]:
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]


'''
Unique Paths II
===============

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths
would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.

Note: m and n will be at most 100.
'''


class Solution(object):
    '''算法思路：

    dp，凡是路过障碍物的统统设为 0
    '''
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = map(len, (obstacleGrid, obstacleGrid[0]))
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j]:
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]


s = Solution()
print s.uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])
