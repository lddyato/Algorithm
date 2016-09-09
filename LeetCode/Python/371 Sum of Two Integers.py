# -*- coding: utf-8 -*-

"""
Sum of Two Integers
===================

Calculate the sum of two integers a and b, but you are not allowed to use the
operator + and -.

Example:

Given a = 1 and b = 2, return 3.
"""


class Solution(object):
    def add(self, a, b):
        for _ in xrange(32):
            a, b = a ^ b, (a & b) << 1
        return a

    def getSum(self, a, b):
        s = self.add(a, b) & 0xFFFFFFFF

        # if sum is negative, we should translate two's complement to
        # the true form
        if s & 0x80000000:
            return -self.add(~(s & 0x7FFFFFFF) & 0x7FFFFFFF, 1)

        return s


s = Solution()
print s.getSum(-9, 10)
