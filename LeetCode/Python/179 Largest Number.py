# -*- coding: utf-8 -*-

'''
Largest Number
==============

Given a list of non negative integers, arrange them such that they form the
largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note:
- The result may be very large, so you need to return a string instead of
  an integer.
'''


class Solution(object):
    '''算法思路：

    设计 compare 函数即可
    '''
    def largestNumber(self, nums):
        return ''.join(sorted(
            map(str, nums),
            lambda x, y: [1, -1][x + y > y + x])
        ).lstrip('0') or '0'



s = Solution()
print s.largestNumber([3, 30, 34, 5, 9])
