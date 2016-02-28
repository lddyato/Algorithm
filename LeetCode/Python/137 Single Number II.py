# -*- coding: utf-8 -*-

'''
Single Number II
================

Given an array of integers, every element appears three times except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?
'''


class Solution(object):
    '''算法思路：

    查看第 i 位 1 的个数是否能够被 3 整除，如果能整除那么第 i 位为0，否则为 1，由于
    python 中符号位在左边无穷远处，因此只能统计负数的个数以便得到最终结果的符号位
    '''
    def singleNumber(self, nums):
        r = 0
        for i in xrange(32):
            mask = 1 << i
            if sum([bool(mask & abs(num)) for num in nums]) % 3:
                r |= mask
        return -r if len(filter(lambda x: x < 0, nums)) % 3 else r


class Solution(object):
    '''算法思路：

    https://leetcode.com/discuss/43377/the-simplest-solution-ever-with-clear-explanation
    '''
    def singleNumber(self, nums):
        ones, twos = 0, 0

        for i in nums:
            ones = (ones ^ i) & ~twos
            twos = (twos ^ i) & ~ones

        return ones


s = Solution()
print s.singleNumber([2, 3, 3, 3])
