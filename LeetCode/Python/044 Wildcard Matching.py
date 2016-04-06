# -*- coding: utf-8 -*-

'''
Wildcard Matching
=================

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:

isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''


def cache(f):
    def method(obj, s, p, i, j):
        key = '{}:{}'.format(i, j)
        if key not in obj.cache:
            obj.cache[key] = f(obj, s, p, i, j)
        return obj.cache[key]
    return method


class Solution(object):
    '''算法思路：

    DFS + cache
    '''
    def __init__(self):
        self.cache = {}

    @cache
    def dfs(self, s, p, i, j):
        m, n = map(len, (s, p))

        if i == m and j == n:
            return True

        if i < m and j == n:
            return False

        if i == m and j < n:
            return p[j] == '*' and self.dfs(s, p, i, j + 1)

        if p[j] == '?' or s[i] == p[j]:
            return self.dfs(s, p, i + 1, j + 1)

        if p[j] == '*':
            return (self.dfs(s, p, i, j + 1) or
                    self.dfs(s, p, i + 1, j + 1) or
                    self.dfs(s, p, i + 1, j))

        return False

    def isMatch(self, s, p):
        if len(p) - p.count('*') > len(s):
            return False

        return self.dfs(s, p, 0, 0)


class Solution(object):
    '''算法思路：

    动态规划，同第 10 题差不多
    '''
    def isMatch(self, s, p):
        m, n = map(len, (s, p))

        if n - p.count('*') > m:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(n):
            dp[0][j + 1] = p[j] == '*' and dp[0][j]

        for i in range(m):
            for j in range(n):
                if s[i] == p[j] or p[j] == '?':
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j] or dp[i][j + 1]

        return dp[-1][-1]


s = Solution()
print s.isMatch("", "*")
