# -*- coding: utf-8 -*-

'''
Longest Valid Parentheses
=========================

Given a string containing just the characters '(' and ')', find the length of
the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has
length = 2.

Another example is ")()())", where the longest valid parentheses substring is
"()()", which has length = 4.
'''


class Solution(object):
    '''算法思路：

    动态规划，dp[i] 表示以 s[i] 结尾的最长 parentheses，那么:
    - s[i] == '('，dp[i] = 0
    - s[i] == ')
      - s[i - dp[i - 1] - 1] == '(' 时，dp[i] = dp[i - 1] + 2 + dp[left - 1]
      - 否则, dp[i] = 0
    '''
    def longestValidParentheses(self, s):
        dp = [0] * len(s)
        for i in xrange(1, len(s)):
            if s[i] == ')':
                left = i - dp[i - 1] - 1
                if left >= 0 and s[left] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[left - 1]
                    continue
            dp[i] = 0

        return max(dp or [0])


s = Solution()
print s.longestValidParentheses('(()))())(')
