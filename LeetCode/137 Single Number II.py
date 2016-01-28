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
