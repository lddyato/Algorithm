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


s = Solution()
print s.singleNumber([2, 3, 2, 3, 23])
