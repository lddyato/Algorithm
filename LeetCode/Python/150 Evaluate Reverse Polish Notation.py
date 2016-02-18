# -*- coding: utf-8 -*-

'''
Evaluate Reverse Polish Notation
================================

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another
expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''


import operator


class Solution(object):
    '''算法思路：

    逆波兰表达式，用栈辅助，需要注意的一点是除法且商为负数时的结果
    '''
    def evalRPN(self, tokens):
        stack, maps = [], {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.div
        }

        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
                continue

            b, a = stack.pop(), stack.pop()

            r = maps[t](a, b)
            if t == '/' and r < 0 and a % b:
                r += 1

            stack.append(r)

        return stack[0]


s = Solution()
print s.evalRPN(["4","-2","/","2","-3","-","-"])
