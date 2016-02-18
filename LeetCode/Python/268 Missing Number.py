# -*- coding: utf-8 -*-

'''
Missing Number
==============

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it
using only constant extra space complexity?
'''


class Solution(object):
    '''算法思路：

    观察 arrary 数值 i 的范围与 array 长度 n 的关系为 0 <= i <= n，两者长度相差 1
    因此把 i 处的值设为 True，最后找出 arrary 里边第一个不为 True 的值，如果全为
    True，那么结果为没有保存在 arrary 里的 n
    '''
    def missingNumber(self, nums):
        n = len(nums)
        for i in xrange(n):
            current = nums[i]
            while current is not True and current < n:
                next = nums[current]
                nums[current] = True
                current = next

        for i, v in enumerate(nums):
            if v is not True:
                return i

        return n


s = Solution()
print s.missingNumber([])
