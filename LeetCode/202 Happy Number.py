# -*- coding: utf-8 -*-

'''
Happy Number
===========

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with
any positive integer, replace the number by the sum of the squares of its
digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for
which this process ends in 1 are happy numbers.

Example: 19 is a happy number

    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
'''


class Solution(object):
    '''算法思路：

    如果不是 happy number，那么平方和循环为：4，16，37，58，89，145，42，20
    '''
    def isHappy(self, n):
        if n in [1, 4]:
            return n == 1

        s = 0
        while n > 0:
            n, mod = divmod(n, 10)
            s += mod ** 2

        return self.isHappy(s)

s = Solution()
print s.isHappy(19)
