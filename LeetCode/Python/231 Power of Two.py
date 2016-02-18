# -*- coding: utf-8 -*-

'''
Power of Two
============

Given an integer, write a function to determine if it is a power of two.
'''


class Solution(object):
    '''算法思想：

    `Power of Two`的意思是 2 的次幂，而不是某个数的平方
    '''
    def isPowerOfTwo(self, n):
        return n > 0 and not n & (n - 1)


s = Solution()
print s.isPowerOfTwo(3)
