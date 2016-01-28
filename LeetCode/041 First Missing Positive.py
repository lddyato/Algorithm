# -*- coding: utf-8 -*-

'''
First Missing Positive
======================

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''


class Solution(object):
    '''算法思路：

    将 nums 里边的数字转化为 hash，然后从小到大依次判断 first 是否在 hash 中

    Time: O(n)
    Space: O(n)
    '''
    def firstMissingPositive(self, nums):
        first, record = 1, {n: 0 for n in nums}
        while first in record:
            first += 1
        return first


class Solution(object):
    '''算法思路：

    观察到一个现象，first 一定在 [1, len(nums) + 1] 之间，因为 nums 最多占据前
    len(nums) 个正整数
    '''
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in xrange(n):
            cursor = nums[i]
            while cursor is not True and 1 <= cursor <= n:
                if nums[cursor - 1] is True:
                    break

                next = nums[cursor - 1]
                nums[cursor - 1] = True
                cursor = next

        for i, v in enumerate(nums):
            if v is not True:
                return i + 1

        return n + 1


s = Solution()
print s.firstMissingPositive([2, 2])
