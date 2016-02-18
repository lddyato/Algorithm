# -*- coding: utf-8 -*-

'''
Gray Code
=========

The gray code is a binary numeral system where two successive values differ in
only one bit.

Given a non-negative integer n representing the total number of bits in the
code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

    00 - 0
    01 - 1
    11 - 3
    10 - 2

Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the
above definition.

For now, the judge is able to judge based on one instance of gray code
sequence. Sorry about that.
'''


class Solution(object):
    '''算法思路：

    递归：f(n) = [[0] + i for i in f(n-1)] + [[1] + i for i in f(n-1)[::-1]]
    '''
    def genCode(self, n):
        if n == 1:
            return [[0], [1]]

        base = self.genCode(n - 1)

        return sum([
            map(lambda i: [prefix] + i, b)
            for prefix, b in ((0, base), (1, base[::-1]))
        ], [])

    def grayCode(self, n):
        return map(
            lambda i: int(''.join(map(str, i)), 2),
            self.genCode(n)
        ) if n else [0]


s = Solution()
print s.grayCode(2)
