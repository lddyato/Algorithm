# -*- coding: utf-8 -*-

'''
Reverse Integer
===============

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''


class Solution(object):
    '''算法思路：

    注意：反转后是否有可能会超出 int 范围
    '''
    def reverse(self, x):
        max, min = pow(2, 31) - 1, -pow(2, 31)

        negative = False
        if x < 0:
            x = -x
            negative = True

        x = str(x)[::-1].lstrip('0')

        i, sum, base = len(x) - 1, 0, 1
        while i >= 0:
            plus = (ord(x[i]) - 48) * base
            if (negative and -min - plus < sum) or (
                    not negative and max - plus < sum):
                return 0

            sum += plus
            base *= 10
            i -= 1

        if negative:
            sum = -sum
        return sum


s = Solution()
print s.reverse(1534236469)
