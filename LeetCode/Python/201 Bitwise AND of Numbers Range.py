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

    找到从 m 到 n，第 k 位 0 的个数

    详细解释已 post 到 leetcode 上：
    https://leetcode.com/discuss/89212/counting-zero-solution-different-from-all-the-others
    '''
    def countOne(self, num, k):
        cycles, num, mask = num >> k + 1, num & ((1 << k + 1) - 1), 1 << k
        return cycles * mask + (((num & ~mask) + 1) if num & mask else 0)

    def countZero(self, num, k):
        cycles, num, mask = num >> k + 1, num & ((1 << k + 1) - 1), 1 << k
        return cycles * mask + (mask if num & mask else (num + 1))

    def rangeBitwiseAnd(self, m, n):
        r, mask = 0, 1
        for i in xrange(32):
            if self.countZero(n, i) - self.countZero(m - 1, i) == 0:
                r |= mask
            mask <<= 1
        return r


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


s = Solution()
print s.rangeBitwiseAnd(6, 7)
