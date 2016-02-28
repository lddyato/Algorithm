# -*- coding: utf-8 -*-

'''
Single Number III
=================

Given an array of numbers nums, in which exactly two elements appear only once
and all the other elements appear exactly twice. Find the two elements that
appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is
also correct.

Your algorithm should run in linear runtime complexity. Could you implement it
using only constant space complexity?
'''


class Solution(object):
    '''算法思路：

    利用 hash 记录每个数字出现的次数
    '''
    def singleNumber(self, nums):
        records = {}
        for n in nums:
            records[n] = records.setdefault(n, 0) + 1
            if records[n] > 1:
                del records[n]

        return records.keys()


class Solution(object):
    '''算法思路：

    首先找到 a, b 第几位不一样，然后根据这一位划分为两个 part，每个 part 相异或即可
    得到结果
    '''
    def singleNumber(self, nums):
        xor = reduce(lambda x, y: x ^ y, nums, 0)

        mask = 1
        while not xor & 1:
            xor >>= 1
            mask <<= 1

        zero, one = 0, 0
        for num in nums:
            if num & mask:
                one ^= num
            else:
                zero ^= num
        return zero, one


s = Solution()
print s.singleNumber([1, 0, 0, 2])
