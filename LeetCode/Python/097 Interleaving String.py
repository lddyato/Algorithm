# -*- coding: utf-8 -*-

'''
Interleaving String
===================

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''


def cache(f):
    def method(obj, s1, s2, s3, i, j, k):
        key = (i, j, k)
        if key not in obj.cache:
            obj.cache[key] = f(obj, s1, s2, s3, i, j, k)
        return obj.cache[key]
    return method


class Solution(object):
    def __init__(self):
        self.cache = {}

    @cache
    def dfs(self, s1, s2, s3, i, j, k):
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True

        if (i < len(s1) and s1[i] == s3[k] and
                self.dfs(s1, s2, s3, i + 1, j, k + 1)):
            return True

        if (j < len(s2) and s2[j] == s3[k] and
                self.dfs(s1, s2, s3, i, j + 1, k + 1)):
            return True

        return False

    def isInterleave(self, s1, s2, s3):
        '''算法思路：

        DFS + cache
        '''
        if sum(map(len, (s1, s2))) != len(s3):
            return False
        return self.dfs(s1, s2, s3, 0, 0, 0)


class Solution(object):
    '''算法思路：

    动态规划，一般用 DFS + cache 的问题都可以用 DP
    '''
    def isInterleave(self, s1, s2, s3):
        m, n, k = map(len, (s1, s2, s3))
        if m + n != k:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i + j == 0:
                    dp[i][j] = True
                    continue

                if i - 1 >= 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True

                if j - 1 >= 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True

        return dp[-1][-1]


s = Solution()
print s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
