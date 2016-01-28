# -*- coding: utf-8 -*-

'''
Basic Calculator
================

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus
+ or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:

"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

Note: Do not use the eval built-in library function.
'''


class Solution(object):
    '''算法思路：

    利用栈，既可以先把中缀表达式转换为后缀表达式，然后在计算，或者直接计算
    '''
    def operate(self, operands, operators):
        import operator
        execute = {'+': operator.add, '-': operator.sub}

        while operators and operators[-1] != '(':
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
                self.operate(operands, operators)
                operators.append(s[i])
            i += 1

        self.operate(operands, operators)
        return operands[-1]


s = Solution()
print s.calculate('1 + 1')
print s.calculate(' 2-1 + 2 ')
print s.calculate('(1+(4+5+2)-3)+(6+8)')
