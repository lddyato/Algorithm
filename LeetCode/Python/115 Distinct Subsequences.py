# -*- coding: utf-8 -*-

'''
Distinct Subsequences
=====================

Given a string S and a string T, count the number of distinct subsequences of
T in S.

A subsequence of a string is a new string which is formed from the original
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters. (ie, "ACE" is a subsequence of
"ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''


class Solution(object):
    '''算法思路：

    DFS，从前往后遍历 s，如果 s[i] == t[0], 则可以选择匹配或者跳过，中间结果缓存起来

    结果：勉强 AC
    '''
    def search(self, s, t, cache):
        key = '{}:{}'.format(s, t)
        if key in cache:
            return cache[key]

        if not t:
            return 1

        r = 0
        for i in xrange(len(s) - len(t) + 1):
            if s[i] == t[0]:
                r += self.search(s[i + 1:], t[1:], cache)

        cache[key] = sum([
            self.search(s[i + 1:], t[1:], cache)
            for i in xrange(len(s) - len(t) + 1)
            if s[i] == t[0]
        ])

        return cache[key]

    def numDistinct(self, s, t):
        return self.search(s, t, {})


class Solution(object):
    '''算法思路：

    动态规划，dp[i][j] 表示 从 s[:i] 到 t[:j] 的个数，可以理解为上面方法的迭代写法，
    效率是上面写法的 10 倍左右
    '''
    def numDistinct(self, s, t):
        m, n = map(len, (t, s))
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(m):
            for j in range(i, n):
                if t[i] == s[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]

        return dp[-1][-1]



s = Solution()
print s.numDistinct("", "")
