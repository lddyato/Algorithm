# -*- coding: utf-8 -*-

'''
Regular Expression Matching
===========================

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:

isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''


def cache(f):
    def method(obj, s, p):
        key = '{}:{}'.format(s, p)
        if key not in obj.cache:
            obj.cache[key] = f(obj, s, p)
        return obj.cache[key]
    return method


class Solution(object):
    '''算法思路：

    DFS + cache
    '''
    def __init__(self):
        self.cache = {}

    @cache
    def isMatch(self, s, p):
        m, n = map(len, (s, p))

        if m == 0:
            if n == 0:
                return True
            if n > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])
            return False

        if (m == 0) + (n == 0) == 1:
            return False

        if n > 1 and p[1] == '*':
            if p[0] == '.' or s[0] == p[0]:
                return (self.isMatch(s[1:], p[2:]) or
                        self.isMatch(s[1:], p) or
                        self.isMatch(s, p[2:]))

            return self.isMatch(s, p[2:])

        if p[0] == '.' or s[0] == p[0]:
            return self.isMatch(s[1:], p[1:])

        return False


class Solution(object):
    '''算法思路：

    动态规划，dp[i][j] 表示 s[:i] 和 p[:j] 之间是否匹配，然后根据 p[j - 1] 是不是
    '*' 来进一步断定
    '''
    def isMatch(self, s, p):
        m, n = map(len, (s, p))

        dp = [[False] * (n + 1) for _ in xrange(m + 1)]
        dp[0][0] = True

        for i in xrange(m + 1):
            for j in xrange(1, n + 1):
                if p[j - 1] != '*':
                    dp[i][j] = (
                        i > 0 and dp[i - 1][j - 1] and
                        (p[j - 1] == '.' or p[j - 1] == s[i - 1])
                    )
                else:
                    dp[i][j] = (
                        (j > 1 and dp[i][j - 2]) or
                        (i > 0 and dp[i - 1][j] and
                            (j > 1 and p[j - 2] == '.' or s[i - 1] == p[j - 2]))
                    )
        return dp[m][n]


s = Solution()
print s.isMatch('', '.*c*')
