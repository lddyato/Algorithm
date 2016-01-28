# -*- coding: utf-8 -*-

'''
Pascal's Triangle
=================

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution(object):
    '''算法思路：

    每一组为左右对角线之和
    '''
    def generate(self, numRows):
        if numRows <= 0:
            return []

        r = [[1]]
        [r.append(
            [(i > 0 and r[-1][i-1] or 0) + (i < len(r[-1]) and r[-1][i] or 0)
             for i in xrange(len(r[-1]) + 1)])
            for _ in xrange(1, numRows)]

        return r


class Solution(object):
    '''算法思路：

    利用组合
    '''
    def generate(self, numRows):
        import math

        return [[
            math.factorial(row) / math.factorial(i) / math.factorial(row - i)
            for i in xrange(row + 1)
        ] for row in xrange(numRows)]


s = Solution()
print s.generate(2)
