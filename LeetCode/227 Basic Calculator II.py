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

    同 227，不过增加了优先级
    '''
    def operate(self, operands, operators, currentOperator=None):
        import operator

        priority = {None: -1, '+': 0, '-': 0, '*': 1, '/': 1}
        execute = {
            '+': operator.add, '-': operator.sub,
            '*': operator.mul, '/': operator.div
        }

        while (operators and operators[-1] != '(' and
                priority[currentOperator] <= priority[operators[-1]]):
            o = operators.pop()
            b = operands.pop()
            a = operands.pop()

            operands.append(execute[o](a, b))

    def calculate(self, s):
        operands, operators = [], []

        i, length = 0, len(s)
        while i < length:
            if s[i] == ' ':
                i += 1
                continue

            if s[i].isdigit():
                operand = ''
                while i < length and s[i].isdigit():
                    operand += s[i]
                    i += 1
                i -= 1
                operands.append(int(operand))
            elif s[i] == '(':
                operators.append('(')
            elif s[i] == ')':
                self.operate(operands, operators)
                operators.pop()
            else:
                self.operate(operands, operators, s[i])
                operators.append(s[i])
            i += 1

        self.operate(operands, operators)
        return operands[-1]


s = Solution()
print s.calculate(' 3+5 / 2 ')
