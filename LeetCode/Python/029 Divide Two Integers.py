# -*- coding: utf-8 -*-

'''
Divide Two Integers
===================

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''


class Solution(object):
    '''算法思路：

    找出最大能够减的 divisor 的 2^n 倍数，然后从 n 到 0，依次看能否减，如果能够减得话，
    累积计算 2^n 的和
    '''
    def divide(self, dividend, divisor):
        MAX_INT, MIN_INT = 2 ** 31 - 1, -2 ** 31

        if divisor == 0 or dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negative = dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0
        dividend, divisor = abs(dividend), abs(divisor)

        shift = 0
        while 1:
            if divisor << 1 > dividend:
                break

            divisor <<= 1
            shift += 1

        r = 0
        while shift >= 0:
            if dividend >= divisor:
                dividend -= divisor
                r += 1 << shift

            shift -= 1
            divisor >>= 1

        return -r if negative else r


s = Solution()
print s.divide(100, -45)
