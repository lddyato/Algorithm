# -*- coding: utf-8 -*-

'''
Power of Two
============

Given an integer, write a function to determine if it is a power of two.
'''


class Solution(object):
    '''算法思路：

    num = An*2^n + .... + A3*2^3 + A2*2^2 + A1*2^1

    如果 num 是 2^n 那么除了 An == 1，剩余的 Ai 都是 0
    '''
    def isPowerOfTwo(self, n):
        bit = 1
        while bit < n:
            bit <<= 1
        return bit == n


class Solution(object):
    '''算法思想：

    同上，都是利用这个特点
    '''
    def isPowerOfTwo(self, n):
        return n > 0 and not n & (n - 1)


import math


class Solution(object):
    '''算法思路：

    如果 n = 2^k，那么 k 必须是整数，只需判断这一点就ok了
    '''
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        r = math.log(n, 2)
        return abs(round(r) - r) <= 1e-10


s = Solution()
print s.isPowerOfTwo(3)
