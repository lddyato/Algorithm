# -*- coding: utf-8 -*-

'''
Pascal's Triangle II
====================

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''


import math


class Solution(object):
    def getRow(self, rowIndex):
        return [math.factorial(rowIndex) / math.factorial(i) /
                math.factorial(rowIndex - i) for i in xrange(rowIndex + 1)]


s = Solution()
print s.getRow(1)
