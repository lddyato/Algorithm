# -*- coding: utf-8 -*-

'''
Basic Calculator II
===================

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators
and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:

"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

Note: Do not use the eval built-in library function.
'''


class Solution(object):
    '''算法思路：

    同 224
    '''
    def RPN(self, expression):
        priority = {'+': 0, '-': 0, '*': 1, '/': 1}
        stack, i, n, r = [], 0, len(expression), []

        while i < n:
            if expression[i].isdigit():
                num = []
                while i < n and expression[i].isdigit():
                    num.append(expression[i])
                    i += 1
                r.append(int(''.join(num)))
                continue

            if expression[i] == '(':
                stack.append('(')
            elif expression[i] == ')':
                while stack[-1] != '(':
                    r.append(stack.pop())
                stack.pop()
            elif expression[i] in priority:
                while (stack and stack[-1] != '(' and
                        priority[expression[i]] <= priority[stack[-1]]):
                    r.append(stack.pop())
                stack.append(expression[i])
            i += 1

        r += stack[::-1]
        return r

    def calculate(self, s):
        rpn, stack = self.RPN(s), []

        operations = {
            '+': operator.add, '-': operator.sub,
            '*': operator.mul, '/': operator.div}

        for item in rpn:
            if isinstance(item, int):
                stack.append(item)
            else:
                b = stack.pop()
                a = stack.pop()

                stack.append(operations[item](a, b))
        return stack[0]


s = Solution()
print s.calculate(' 3+5 / 2 ')
