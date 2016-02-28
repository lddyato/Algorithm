# -*- coding: utf-8 -*-

'''
Reverse Bits
============

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as
00000010100101000001111010011100), return 964176192 (represented in binary as
00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
'''


class Solution(object):
    '''算法思路：

    求出各个位的系数，然后反转后得到结果
    '''
    def reverseBits(self, n):
        bits = []
        for i in xrange(32):
            bits.append(n & 1)
            n >>= 1

        r, mask = 0, 1
        for i in xrange(31, -1, -1):
            if bits[i]:
                r |= mask
            mask <<= 1
        return r


class Solution(object):
    '''算法思路：

    同上，只不过求系数的同时，求出结果
    '''
    def reverseBits(self, n):
        r = 0
        for _ in xrange(32):
            r <<= 1
            r |= n & 1
            n >>= 1
        return r


s = Solution()
print s.reverseBits(1)
