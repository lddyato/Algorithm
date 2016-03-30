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

    该解法是通用解法，包含括号和四则运算，逆波兰表达式中栈自底向上符号优先级是递增的

    note: RPN => Reversed Polish Notation，即逆波兰表达式
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
print s.calculate('1 + 1')
print s.calculate(' 2-1 + 2 ')
print s.calculate('(1+(4+5+2)-3)+(6+8)')
