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
    def reverseBits(self, n):
        count, r = 0, 0
        while count < 32:
            last = n & 1
            n >>= 1

            r |= last
            r <<= 1

            count += 1

        r >>= 1
        return r


s = Solution()
print s.reverseBits(1)
