# -*- coding: utf-8 -*-

'''
Write a function that takes an unsigned integer and returns the number of ’1'
bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation
00000000000000000000000000001011, so the function should return 3.
'''


class Solution(object):
    '''算法思路：

    统计 1 的个数
    '''
    def hammingWeight(self, n):
        r = 0
        while n:
            r += n & 1
            n >>= 1
        return r


s = Solution()
print s.hammingWeight(3)
