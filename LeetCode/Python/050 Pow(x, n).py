# -*- coding: utf-8 -*-

'''
Pow(x, n)
=========

Implement pow(x, n).
'''


class Solution(object):
    '''算法思路：

    快速幂

    注意: 要考虑到 n 为负数的情况
    '''
    def pow(self, x, n):
        result = 1
        while n:
            if n & 1:
                result *= x

            x *= x
            n >>= 1

        return result

    def myPow(self, x, n):
        if n == 0:
            return 1

        if n < 0:
            return 1.0/self.pow(x, -n)

        return self.pow(x, n)


s = Solution()
print pow(34.00515, -1)
print s.myPow(34.00515, -1)
