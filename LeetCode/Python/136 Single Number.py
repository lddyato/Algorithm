# -*- coding: utf-8 -*-

'''
Single Number
=============

Given an array of integers, every element appears twice except for one. Find
that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?
'''


class Solution(object):
    '''算法思路：

    用 hash 记录每个 number 的次数

    不好的地方：用了 extra memory
    '''
    def singleNumber(self, nums):
        record = {}
        for i in nums:
            record[i] = record.setdefault(i, 0) + 1
            if record[i] > 1:
                del record[i]

        return record.keys()[0]


class Solution(object):
    '''算法思路：

    利用位运算，异或的逆运算是 itselft 即 a ^ b ^ b = a
    '''
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums, 0)


class Solution(object):
    '''算法思路：

    同 II
    '''
    def singleNumber(self, nums):
        r, k = 0, 2
        for i in xrange(32):
            mask = 1 << i
            if sum([bool(mask & abs(num)) for num in nums]) % k:
                r |= mask
        return -r if len(filter(lambda x: x < 0, nums)) % k else r


s = Solution()
print s.singleNumber([2, 3, 2, 3, 23])
