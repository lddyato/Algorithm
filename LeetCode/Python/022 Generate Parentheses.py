# -*- coding: utf-8 -*-

'''
Generate Parentheses
====================

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''


class Solution(object):
    '''算法思路：

    DFS，每走一步有两种选择，左括号或者右括号，记录每一步的状态
    '''
    def dfs(self, parentheses, lack, open, r):
        if lack == 0 and open == 0:
            r.append(parentheses)
            return

        if lack > 0:
            self.dfs(parentheses + '(', lack - 1, open + 1, r)

        if open > 0:
            self.dfs(parentheses + ')', lack, open - 1, r)

    def generateParenthesis(self, n):
        r = []
        self.dfs('', n, 0, r)
        return r


s = Solution()
print s.generateParenthesis(3)
