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

    回溯及递归
    '''
    def generate(self, stack, used, n, step):
        '''main func

        ::params::
          - stack: 保存当前尚未被弹出的 '('
          - used: 当前已经使用的 '(' 的个数
          - n: n
          - step: 当前深度，最大深度为 2*n
        '''
        if not stack and used < n:
            stack.append('(')
            used += 1
            return ['(' + p for p in
                    self.generate(stack[:], used, n, step + 1)]

        r = []
        if used < n:
            stack.append('(')
            used += 1

            r += ['(' + p for p in self.generate(stack[:], used, n, step + 1)]

            del stack[-1]
            used -= 1

        if step <= 2 * n:
            del stack[-1]
            if step + 1 <= 2 * n:
                r += [')' + p for p in
                      self.generate(stack[:], used, n, step + 1)]
            else:
                r += [')']

        return r

    def generateParenthesis(self, n):
        return self.generate([], 0, n, 1)


class Solution(object):
    '''算法思路：

    这种解法是对上述解法的提炼

    https://leetcode.com/discuss/25725/7-lines-in-python-44-ms
    '''
    def generateParenthesis(self, n, open=0):
        if n == 0:
            return [')' * open]

        if open == 0:
            return ['(' + p for p in self.generateParenthesis(n - 1, open + 1)]

        return ['(' + p for p in self.generateParenthesis(n - 1, open + 1)] + [
                ')' + p for p in self.generateParenthesis(n, open - 1)]


s = Solution()
print s.generateParenthesis(3)
