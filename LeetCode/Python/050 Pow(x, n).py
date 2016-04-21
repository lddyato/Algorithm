# -*- coding: utf-8 -*-

'''
Pow(x, n)
=========

Implement pow(x, n).
'''


class Solution(object):
    '''算法思路：

    快速幂运算，也可以这样理解:

    n = k0*2^0 + k1*2^1 + k2*2^2 + ... + kn*2^n

    x ^ n
    = x ^ (k0*2^0 + k1*2^1 + k2*2^2 + ... + kn*2^n)
    = (x^(2^0))^k0 * (x^(2^1))^k1 * (x^(2^2))^k2 * ... * (x^(2^n))^kn

    因此，计算出 k0, k1, k2, ..., kn 按照公式即可求出 x ^ n
    '''
    def myPow(self, x, n):
        if n < 0:
            x = 1.0 / x if x else x
            n = -n

        r, base = 1, x
        while n:
            r *= base if n & 1 else 1
            n >>= 1
            base *= base
        return r


s = Solution()
print pow(34.00515, -1)
print s.myPow(34.00515, -1)
