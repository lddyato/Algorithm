# -*- coding: utf-8 -*-

'''
Different Ways to Add Parentheses
=================================

Given a string of numbers and operators, return all possible results from
computing all the different possible ways to group numbers and operators.
The valid operators are +, - and *.

Example 1
Input: "2-1-1".

    ((2-1)-1) = 0
    (2-(1-1)) = 2

Output: [0, 2]

Example 2
Input: "2*3-4*5"

    (2*(3-(4*5))) = -34
    ((2*3)-(4*5)) = -14
    ((2*(3-4))*5) = -10
    (2*((3-4)*5)) = -10
    (((2*3)-4)*5) = 10

Output: [-34, -14, -10, -10, 10]
'''


import operator


class Solution(object):
    '''算法思路：

    对于每一个符号，分别算出左边和右边的结果，然后左右分别相乘
    '''
    def search(self, expr):
        return expr if len(expr) == 1 else sum([[
            expr[i](p, q)
            for p in self.search(expr[:i])
            for q in self.search(expr[i+1:])
        ] for i in xrange(1, len(expr), 2)], [])

    def diffWaysToCompute(self, input):
        maps = {'+': operator.add, '-': operator.sub, '*': operator.mul}

        expr, digits, i, genNum = [], [], 0, lambda ds: int(''.join(ds))
        for c in input:
            if c.isdigit():
                digits.append(c)
            else:
                expr, digits = expr + [genNum(digits), maps[c]], []

        expr += [genNum(digits)]
        return self.search(expr)


s = Solution()
print s.diffWaysToCompute('2*3-4*5')
