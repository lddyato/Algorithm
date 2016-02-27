# -*- coding: utf-8 -*-

'''
Divide Two Integers
===================

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''


def getA(x):
    '''
    任何整数都能够用 a0*2^0 + a1*2^1 + a2*2^2 + ...... an*2^n 来表示，随便给出一个
    数，因此计算出来 a0, a1, ..., an，也就计算出来 x 了
    '''
    bit = 1
    while bit < x:
        bit <<= 1

    A = []
    while bit:
        a = bit <= x
        A.append(a)

        if a:
            x -= bit
        bit >>= 1
    return A


class Solution(object):
    '''算法思路：

    dividend = div * divisor + mod

    div 可以用 a0*2^0 + a1*2^1 + a2*2^2 + ...... an*2^n 表示，那么根据上述思想，就
    有如下解法

    找出最大能够减的 divisor 的 2^n 倍数，然后从 n 到 0，依次看能否减，如果能够减得话，
    累积计算 2^n 的和
    '''
    def divide(self, dividend, divisor):
        MAX_INT, MIN_INT = 2 ** 31 - 1, -2 ** 31

        if divisor == 0 or dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = map(abs, (dividend, divisor))

        bit = 1
        while divisor < dividend:
            divisor <<= 1
            bit <<= 1

        r = 0
        while bit:
            if divisor <= dividend:
                dividend -= divisor
                r += bit

            bit >>= 1
            divisor >>= 1

        return -r if negative else r


s = Solution()
print s.divide(100, -45)
