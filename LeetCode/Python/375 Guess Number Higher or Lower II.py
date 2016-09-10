# -*- coding: utf-8 -*-


class Solution(object):
    """算法思路：

    记忆化DFS搜索，Top-down
    """
    def dfs(self, start, end):
        if start >= end:
            return 0

        if start + 1 == end:
            return start

        if self.record[start][end] is None:
            self.record[start][end] = min(
                i + max(self.dfs(start, i - 1), self.dfs(i + 1, end))
                for i in xrange(start, end + 1)
            )

        return self.record[start][end]

    def getMoneyAmount(self, n):
        self.record = [[None] * (n + 1) for _ in xrange(n + 1)]
        return self.dfs(1, n)


class Solution(object):
    """算法思路：

    DP，动态规划，Bottom-up。记忆化搜索其实就是动态规划，思想是一样的，
    写法不一样
    """
    def getMoneyAmount(self, n):
        record = [[0] * (n + 2) for _ in xrange(n + 2)]

        for r in xrange(2, n + 1):
            for start in xrange(1, n - r + 2):
                end = start + r - 1
                record[start][end] = min(
                    i + max(record[start][i - 1], record[i + 1][end])
                    for i in xrange(start, end + 1)
                )

        return record[1][n]
