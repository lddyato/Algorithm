# -*- coding: utf-8 -*-

'''
Bitwise AND of Numbers Range
============================

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
'''


class Solution(object):
    '''算法思路：

    最直接的做法

    结果：TLE
    '''
    def rangeBitwiseAnd(self, m, n):
        return reduce(lambda x, y: x & y, xrange(m + 1, n + 1), m)


class Solution(object):
    '''算法思路：

    求公共前缀

    参考了：https://leetcode.com/discuss/53646/simple-and-easy-to-understand-java-solution
    '''
    def rangeBitwiseAnd(self, m, n):
        bits = 0
        while m != n:
            m >>= 1
            n >>= 1
            bits += 1
        return m << bits


class Solution(object):
    '''算法思路：

    另外一种解法

    https://leetcode.com/discuss/49088/2-line-solution-with-detailed-explanation
    '''
    def rangeBitwiseAnd(self, m, n):
        while m < n:
            n &= n - 1
        return n


s = Solution()
print s.rangeBitwiseAnd(6, 7)
