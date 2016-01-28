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


class Solution(object):
    '''算法思路：

    动态规划，同第 10 题差不多
    '''
    def isMatch(self, s, p):
        m, n = map(len, (s, p))

        if n - p.count('*') > m:
            return False

        dp = [[False] * (n + 1) for _ in xrange(m + 1)]
        dp[0][0] = True

        for i in xrange(m + 1):
            for j in xrange(1, n + 1):
                if p[j - 1] != '*':
                    dp[i][j] = (
                        i > 0 and dp[i - 1][j - 1] and
                        (p[j - 1] == '?' or p[j - 1] == s[i - 1])
                    )
                else:
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[m][n]


s = Solution()
print s.isMatch("", "*")
